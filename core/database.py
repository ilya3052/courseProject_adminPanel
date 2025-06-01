import logging
import os
import sys

import asyncio
import asyncpg
import psycopg as ps
from dotenv import load_dotenv
from psycopg import AsyncConnection

load_dotenv()


class Database:
    _connect: ps.connect = None
    _async_connect: AsyncConnection.connect = None
    _lock = asyncio.Lock()
    _listen_lock = asyncio.Lock()  # <--- добавлено
    _subscribed_channels = set()

    @staticmethod
    def get_connection():
        if Database._connect is None:
            try:
                Database._connect = ps.connect(
                    dbname=os.getenv("DB_NAME"),
                    user=os.getenv("USER"),
                    password=os.getenv("PASSWORD"),
                    host=os.getenv("HOST"),
                    port=os.getenv("PORT")
                )
            except ps.Error:
                logging.critical("Соединение не установлено!")
                sys.exit(1)
        return Database._connect

    @staticmethod
    async def get_async_connection():
        if Database._async_connect is not None:
            return Database._async_connect

        async with Database._lock:
            if Database._async_connect is None:
                try:
                    Database._async_connect = await asyncpg.connect(
                        user=os.getenv("USER"),
                        password=os.getenv("PASSWORD"),
                        database=os.getenv("DB_NAME"),
                        host=os.getenv("HOST"),
                        port=os.getenv("PORT")
                    )
                    logging.info(f"Асинхронное соединение через asyncpg установлено, id: {id(Database._async_connect)}")
                except Exception as e:
                    logging.critical(f"Асинхронное соединение не установлено: {e}")
                    sys.exit(1)

        return Database._async_connect

    @staticmethod
    async def listen_channel(channel_name: str, callback):
        conn = await Database.get_async_connection()

        if channel_name in Database._subscribed_channels:
            logging.info(f"Канал '{channel_name}' уже подписан — пропускаем")
            return

        async with Database._listen_lock:  # 👈 важно
            try:
                await conn.add_listener(channel_name, callback)
                Database._subscribed_channels.add(channel_name)
                logging.info(f"Подписка на канал '{channel_name}' установлена")
            except Exception as e:
                logging.error(f"Ошибка при подписке на канал '{channel_name}': {e}")

    @staticmethod
    async def notify_channel(channel_name: str, payload: str):
        conn = await Database.get_async_connection()
        payload_escaped = payload.replace("'", "''")
        sql = f"NOTIFY {channel_name}, '{payload_escaped}';"

        await conn.execute(sql)
        logging.info(f"Отправлено уведомление на канал '{channel_name}': {payload}")

    @staticmethod
    async def close_connection():
        if Database._connect is not None:
            Database._connect.close()
        if Database._async_connect is not None:
            await Database._async_connect.close()

    @staticmethod
    async def is_user_registered(user_id):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                status = cur.execute(
                    "SELECT 1 FROM users WHERE user_tgchat_id = {} AND user_role = 'user';".format(user_id)).fetchone()[
                    0]
                if status: return True
        except TypeError:
            return False

LOCALIZED_TABLES_NAMES = {
    "users": "Пользователи",
    "client": "Клиенты",
    "courier": "Курьеры",
    "delivery": "Доставки",
    "product": "Товары",
    "order": "Заказы",
}

LOCALIZED_COLUMNS_NAME = {
    "users": {
        "user_id": "ID пользователя",
        "user_tgchat_id": "ID телеграм чата",
        "user_role": "Роль",
        "user_name": "Имя",
        "user_surname": "Фамилия",
        "user_patronymic": "Отчество",
        "user_phonenumber": "Номер телефона",
        "user_tg_username": "Юзернейм",
    },
    "client": {
        "client_id": "ID клиента",
        "fullname": "Полное имя",
        "client_registerdate": "Дата регистрации",
        "client_nickname": "Обращение",
    },
    "courier": {
        "courier_id": "ID курьера",
        "fullname": "Полное имя",
        "courier_rating": "Рейтинг",
        "courier_is_busy_with_order": "Занятость заказом",
    },
    "delivery": {
        "delivery_id": "ID доставки",
        "courier": "Курьер",
        "order_id": "ID заказа",
        "delivery_rating": "Оценка доставки",
    },
    "product": {
        "product_article": "Артикул",
        "product_name": "Название товара",
        "product_category": "Категория",
        "product_price": "Стоимость",
        "product_description": "Описание",
    },
    "order": {
        "order_id": "ID заказа",
        "client": "Клиент",
        "order_status": "Статус",
        "order_address": "Адрес",
        "order_review": "Отзыв",
    },
}

IDENTIFIERS = {
    "users": "user_id",
    "client": "client_id",
    "courier": "courier_id",
    "delivery": "delivery_id",
    "product": "product_article",
    "order": "order_id",
}

FOREIGN_KEYS = {
    "users": [],
    "client": ["user_id"],
    "courier": ["user_id"],
    "delivery": ["courier_id"],
    "product": [],
    "order": ["client_id"],
}

NON_EDITABLE_COLUMNS = {
    "users": ["user_tgchat_id", "user_role"],
    "client": ["user_id", "fullname", "client_registerdate"],
    "courier": ["user_id", "fullname"],
    "delivery": ["courier_id", "order_id", "courier"],
    "product": [],
    "order": ["client_id", "client"],
}

REDACT_IN_MODAL_WINDOW_MODE = {
    "users": [],
    "client": [],
    "courier": [],
    "delivery": [],
    "product": [],
    "order": ["order_status"],
}

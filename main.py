import uuid

from yookassa import Configuration, Payment

Configuration.account_id = '1051288'  # Например, "123456"
Configuration.secret_key = 'test_9dj_MGGU0svpLmFIYNY2cjnoCqIV7gRapE-F_wqXby8'

payment = Payment.create({
    "amount": {
        "value": "100.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.example.com/return_url"
    },
    "capture": True,
    "description": "Заказ №1"
}, uuid.uuid4())

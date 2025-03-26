from django.db import models

from api.validators import validate_phone_number, validate_email


class Client(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Имя и фамилия")
    email = models.CharField(
        max_length=200,
        verbose_name="Почта",
        validators=[validate_email],
    )

    phone_number = models.CharField(
        max_length=50,
        verbose_name="Номер телефона",
        validators=[validate_phone_number]
    )

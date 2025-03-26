# Generated by Django 5.1.7 on 2025-03-26 12:19

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Имя и фамилия')),
                ('email', models.CharField(max_length=200, validators=[api.validators.validate_email], verbose_name='Почта')),
                ('phone_number', models.CharField(max_length=50, validators=[api.validators.validate_phone_number], verbose_name='Номер телефона')),
            ],
        ),
    ]

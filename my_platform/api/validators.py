from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not value.startswith('+7'):
        raise ValidationError("Номер должен начинаться с '+7'.")

    if not value[2:].isdigit() or len(value[2:]) != 10:
        raise ValidationError("Номер должен содержать 10 цифр после '+7'.")


def validate_email(value):
    if not '@' in value:
        raise ValidationError("Почта должна содержать символ '@'.")
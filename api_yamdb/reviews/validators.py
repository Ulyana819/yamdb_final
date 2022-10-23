import datetime as dt

from django.core.exceptions import ValidationError


def validate_me(value):
    if value == 'me':
        raise ValidationError(
            "Выберете другое имя"
        )


def validate_year(year):
    now_dt = dt.date.today()
    if year > now_dt.year:
        raise ValueError(f'Некорректный год {year}')

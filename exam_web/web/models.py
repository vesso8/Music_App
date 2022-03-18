import re

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

def validate_letters_numbers_underscores(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 0


    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_letters_numbers_underscores,
        ),
    )
    email = models.EmailField()
    age = models.IntegerField(
        null = True,
        blank = True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )
class Album(models.Model):
    NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    PRICE_MIN_VALUE = 0.0

    GENRE_TYPES =[(x,x) for x in (POP_MUSIC, JAZZ_MUSIC, RB_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    artist = models.CharField(
        max_length= ARTIST_MAX_LENGTH,
    )
    genre = models.CharField(
        max_length= GENRE_MAX_LENGTH,
        choices=GENRE_TYPES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField()
    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
    def save(self, *args, **kwargs):
        self.price = round(self.price)
        super(Album, self).save(*args, **kwargs)
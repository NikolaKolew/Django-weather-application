from django.db import models

class City(models.Model):
    CITY_MAX_LENGTH = 25
    name = models.CharField(
        max_length= CITY_MAX_LENGTH,
        unique=True,
    )
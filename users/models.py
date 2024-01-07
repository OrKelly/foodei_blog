from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", default='users/default.png', blank=True, null=True, verbose_name="Фотография")
    organisation = models.CharField(null=True, blank=True, verbose_name='Место работы', max_length=200)
    description = models.TextField(null=True, blank=True, verbose_name='Расскажите о себе')


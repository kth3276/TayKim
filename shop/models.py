from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    shop = models.ForeignKey(Shop)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.author


class Item(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


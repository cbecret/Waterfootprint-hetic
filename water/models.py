from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Region(models.Model):
    region_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WaterData(models.Model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    product = models.CharField(max_length=200)
    green = models.FloatField()
    blue = models.FloatField()
    grey = models.FloatField()

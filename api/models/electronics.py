from django.db import models

class Electronic(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)



from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

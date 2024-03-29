from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegetarian = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.name

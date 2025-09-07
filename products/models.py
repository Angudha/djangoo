from django.db import models
from django.db.models import DecimalField
from django.urls import reverse



# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"id": self.id})
        # return f"/search/{self.id}/"

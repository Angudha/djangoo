from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    article_name = models.CharField(max_length=120)
    size = models.CharField(max_length=100)
    date_published = models.DateField()

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"id": self.id})


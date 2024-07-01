from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    publish =models.BooleanField(default=False, verbose_name='Publication')
    date = models.DateTimeField(auto_now=True)
    conten= models.TextField( verbose_name='Text_articles')
    auteur= models.ForeignKey(User, on_delete=models.PROTECT, default="", null=True)
    description = models.TextField(default="", blank=True)
    images = models.ImageField(blank=True, upload_to='images/')

    class Meta:
        verbose_name = "article"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} {self.conten}"

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostModel(models.Model):
    
    author = models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name="Ad:")
    context = models.TextField(verbose_name="Mezmun:")

    def __str__(self):
        return self.title


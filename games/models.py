from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GameContents(models.Model) :
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)

class Comments(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(GameContents, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
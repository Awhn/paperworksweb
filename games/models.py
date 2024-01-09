from django.db import models

# Create your models here.
class GameContents(models.Model) :
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)
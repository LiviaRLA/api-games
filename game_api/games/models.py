from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Developer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='games')
    platforms = models.ManyToManyField(Platform, related_name='games')
    genre = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.title

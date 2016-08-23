from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    sirname = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    username = models.CharField(max_length=50)
    comment = models.CharField(max_length=5000)
    pub_date = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Like(models.Model):
    username = models.CharField(max_length=50)
    comment_id = models.IntegerField()

    def __str__(self):
        return str(self.id)
    

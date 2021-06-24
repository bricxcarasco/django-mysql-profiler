from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.utils.html import mark_safe
import os, random

# Create your models here.

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(characters)) for x in range(10))
    _now = now()

    return 'profile/{0}-{1}-{2}-{3}-{4}-{5}{6}'.format(_now.strftime('%Y'), _now.strftime('%m'), _now.strftime('%d'), instance, basefilename, randomstr, file_extension)

class User(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='First Name')
    last_name = models.CharField(max_length=200, verbose_name='Last Name')
    email = models.CharField(unique=True, max_length=200, verbose_name='Email')
    position = models.CharField(max_length=200, verbose_name='Position')
    image = models.ImageField(upload_to=image_path, default='profile/default.jpeg')
    created_at = models.DateTimeField(default=now())

    def image_tag(self):
        return mark_safe('<img src="/users/media/{0}" width="50" height="50" />'.format(self.image))

    def __str__(self):
        return self.email

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(default='null')
    body = models.TextField(default='null')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now())

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment {0} by {1}'.format(self.body, self.name)


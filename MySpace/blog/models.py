from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class UserInfo(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    birth_date = models.DateTimeField(auto_now_add=False)
    email = models.TextField(max_length=50)
    user = models.OneToOneField(User)


class Topics(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return u'{} @ {}'.format(self.title, self.description)


class Post(models.Model):
    title = models.TextField(max_length=50)
    text = models.TextField(max_length=10000)
    date_added = models.DateTimeField(
        auto_now_add=True)
    topic = models.ForeignKey(Topics)
    acces = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.date_added, self.text)


class UserPostComment(models.Model):
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name='comments')

    class Meta:
        ordering = ['date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)


class Likes(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date_added = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.date_added, self.author, self.post)
    

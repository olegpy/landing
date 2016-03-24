from django.db import models
from django.utils import timezone


class Thumbnail(models.Model):
    header = models.CharField(max_length=50)
    image = models.FileField(upload_to='static/img/uploads/%Y/%m/%d/')
    description = models.TextField()

    def __unicode__(self):
        return self.header


class MainSlider(models.Model):
    image = models.FileField(upload_to='static/img/uploads/%Y/%m/%d/')
    header = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True)
    btn_text = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return u"%s" % self.id


class Review(models.Model):
    image = models.FileField(upload_to='static/img/uploads/%Y/%m/%d/')
    url_video = models.CharField(max_length=25, blank=True)
    author = models.CharField(max_length=25, blank=True)
    header = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.author

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time = models.DateField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','time')



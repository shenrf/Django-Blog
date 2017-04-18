# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Author(models.Model):
    salution = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    headshot = models.ImageField(upload_to='tmp', blank=True, null=True)

    def __str__(self):
        return "{salution}. {first_name} {last_name}".format(
            salution=self.salution, first_name=self.first_name, last_name=self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    publisher = models.ForeignKey('Publisher')
    authors = models.ManyToManyField(Author)
    #quality = models.CharField(max_length=10)
    good = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class BookSearch(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'publication_date']
    list_filter = ('publisher', 'publication_date')
    ordering = ['-publication_date']
    search_fields = ['title']




















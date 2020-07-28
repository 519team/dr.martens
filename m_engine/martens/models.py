# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.contrib.postgres.fields import ArrayField


#  python3 manage.py makemigrations
#  python3 manage.py migrate
# Create your models here.
class ProdPhotos(models.Model):
    path = models.FilePathField()

    def __str__(self):
        return '{}'.format(self.path)


class CatPhotos(models.Model):
    path = models.FilePathField()

    def __str__(self):
        return '{}'.format(self.path)


class BlogPhotos(models.Model):
    path = models.FilePathField()

    def __str__(self):
        return '{}'.format(self.path)


class Review(models.Model):
    username = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique=True)
    location = models.CharField(max_length=20)
    segment = models.CharField(max_length=20)
    overall_rating = models.FloatField()
    pros = models.TextField(blank=True)
    cons = models.TextField(blank=True)
    confirmed = models.DateField()
    published = models.DateField()
    helpful = models.CharField(max_length=10, blank=True)
    photo_path = models.FilePathField(null=True)

    def __str__(self):
        return '{}'.format(str(self.username) + ' ' + str(self.overall_rating))


class Product(models.Model):
    prod_name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=30, unique=True, default=None)
    price = models.FloatField(null=True)
    special_price = models.FloatField(null=True)
    color_name = models.CharField(max_length=30, null=True)
    sizes_male = ArrayField(models.CharField(max_length=6), default=None)
    sizes_female = ArrayField(models.CharField(max_length=6), default=None)
    sizes_juniors = ArrayField(models.CharField(max_length=6), default=None)
    n_comments = models.IntegerField(default=0)
    style = models.FloatField(null=True)
    val4money = models.FloatField(null=True)
    quality = models.FloatField(null=True)
    overall_rating = models.FloatField(null=True)

    def __str__(self):
        return '{}'.format(str(self.prod_name) + '\n' + str(self.color_name))


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique=True)
    type = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(str(self.cat_name) + '\n' + str(self.slug))


class InstPost(models.Model):
    user_link = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique=True)
    photo_path = models.FilePathField()
    prod_slug = models.SlugField(max_length=30, unique=True)
    prod_name = models.CharField(max_length=100)
    prod_photo = models.FilePathField()

class BlogPost(models.Model):
    # into reference and to the title
    title = models.CharField(max_length=70, db_index=True)
    cat_text = models.CharField(max_length=30)
    pvw_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True)
    date_pub = models.DateField(default=None, null=True)
    youtube_link = models.SlugField(default=None, null=True)

    def __str__(self):
        return '{}'.format(str(self.title) + '\n' + str(self.slug))

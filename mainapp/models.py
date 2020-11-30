from django.db import models


class groups(models.Model):
    name = models.CharField(max_length=255)


class list_items(models.Model):
    name_group = models.CharField(max_length=255)
    nmae_item = models.CharField(max_length=255)
    FCs = models.CharField(max_length=255)
    quantity_works = models.IntegerField()


class users(models.Model):
    FCs = models.CharField(max_length=255)
    group = models.CharField(max_length=255, default="teacher")
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class works(models.Model):
    FC = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    FCs = models.CharField(max_length=255)
    name_work = models.CharField(max_length=255)
    link_work = models.CharField(max_length=255)
    error = models.CharField(max_length=255)
    estimation = models.CharField(max_length=255)
    nmae_item = models.CharField(max_length=255)
    message = models.TextField()

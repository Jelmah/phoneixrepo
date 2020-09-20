
from django.db import models
from datetime import datetime


# Create your models here.
class Glasse(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    age_size = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    pwithd = models.IntegerField()
    pwithoutd = models.IntegerField()
    discount = models.CharField(max_length=40)
    rating = models.IntegerField()
    description = models.TextField()
    main_img = models.ImageField(upload_to='postpics/%Y/%m/%d/')
    img_1 = models.ImageField(upload_to='postpics/%Y/%m/%d/', blank=True)
    img_2 = models.ImageField(upload_to='postpics/%Y/%m/%d/', blank=True)
    img_3 = models.ImageField(upload_to='postpics/%Y/%m/%d/', blank=True)
    shipin_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name



class Watche(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    age_size = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    pwithd = models.IntegerField()
    pwithoutd = models.IntegerField()
    discount = models.CharField(max_length=40)
    rating = models.IntegerField()
    description = models.TextField()
    main_img = models.ImageField(upload_to='postpics/%Y/%m/%d/')
    img_1 = models.ImageField(upload_to='postpics/%Y/%m/%d/', blank=True)
    img_2 = models.ImageField(upload_to='postpics/%Y/%m/%d/', blank=True)
    img_3 = models.ImageField(upload_to='postpics/%Y/%m/%d/', blank=True)
    shipin_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
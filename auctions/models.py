from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Create_Listing(models.Model):
    seller = models.CharField(max_length=94)
    product = models.CharField(max_length=94)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=94)

class Active_Listings_Page(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listingid = models.IntegerField()
    Active_Listings_Page = models.IntegerField()

class Comment(models.Model):
    user = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    comment = models.TextField()
    listingid = models.IntegerField()   

class Existlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()

class Alllisting(models.Model):
    listingid = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=64,default=None,blank=True,null=True)         

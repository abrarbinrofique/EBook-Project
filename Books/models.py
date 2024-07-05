from django.db import models
from django.contrib.auth.models import User
from catagory.models import Catagory
# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=100)
    catagory=models.ManyToManyField(Catagory)
    user=models.ManyToManyField(User,blank=True,null=True)
    description=models.TextField(max_length=500)
    price=models.IntegerField()
    image = models.ImageField(upload_to='post/',blank=True,null=True)


class Review(models.Model):
    Bookreview=models.ForeignKey(Book, on_delete=models.CASCADE,blank=True,null=True,related_name='comments')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    text=models.TextField()
    createdate=models.DateTimeField(auto_now_add=True)



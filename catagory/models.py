from django.db import models

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=20) 
    slug=models.SlugField(max_length=50 ,unique=True,blank=True,null=True)



    def __str__(self):
        return self.name
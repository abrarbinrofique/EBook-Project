from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Transaction(models.Model):
    user=models.ForeignKey(User,related_name='transaction', on_delete=models.CASCADE,null=True, default=None)
    amount=models.DecimalField(max_digits=100000,decimal_places=2)
    


class wallet(models.Model):
    user=models.OneToOneField(User,related_name='account', on_delete=models.CASCADE)
    balance=models.DecimalField(max_digits=100000,decimal_places=2,null=True,default=0,blank=True)
   
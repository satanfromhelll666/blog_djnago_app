from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)


class blog_contain(models.Model):
    subject = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True)
    discription = models.CharField(max_length=2000,null=True)
    comment = models.CharField(max_length= 1000,null= True)
    
    
from django.db import models

# Create your models here.

class Contact(models.Model):
    given_name = models.CharField(max_length=100,blank=False)
    family_name = models.CharField(max_length=100,blank=False)
    email_address = models.CharField(max_length=200,blank=False)
    phone_number = models.CharField(max_length=100)
    street = models.TextField()
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)



class ContactManager(models.Manager):
    pass

    
    
    
    
    
    
    
    
    

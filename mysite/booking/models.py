from django.db import models
from django.utils import timezone

class UserManager(models.Manager):
    pass


class BookingManager(models.Manager):
    pass

class User(models.Model):
    objects=UserManager()
    firstName= models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    def __unicode__(self):
        return '{} {}'.format(self.firstName, self.lastName)




class Room(models.Model):    
    price = models.IntegerField(default=0)
    roomType= models.CharField(max_length=100)
    available = True
    def __unicode__(self):
        return '{} {}'.format(self.price, self.roomType)
 
   

class Booking(models.Model):
    created = models.DateField(auto_now_add=True)
    endDate = models.DateField()
    room = models.ForeignKey(Room,related_name='room')
    

        
    
    
    

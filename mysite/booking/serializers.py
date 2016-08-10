from rest_framework import serializers
from booking.models import User,Booking,Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields = ('id','roomType','price')

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=False,read_only=True)  
    class Meta:
        model = Booking
        fields = ('id', 'created','room','endDate')


class UserSerializer(serializers.ModelSerializer):
    class Meta:       
        model = User  
        fields = ('id', 'firstName', 'lastName','email','password')
    
 


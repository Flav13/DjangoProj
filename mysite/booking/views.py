from django.shortcuts import render
from rest_framework import generics
from booking.serializers import UserSerializer, BookingSerializer
from booking.models import Booking,Room,User
from rest_framework import generics

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route




def index_view(request):
    #form_class=ClientForm
    #template_name = 'booking/index.html'
    
    return render(request, 'booking/index.html')


def createUser(request):
    return render(request, 'booking/userDetail.html')
    

def createBooking(request):
    room = Room.objects.all()
    for rooms in room:
        if rooms.available==False:
            room.remove(rooms)
            
    return render(request, 'booking/bookingDetail.html',{
            'room': room,
             })

def authenticateUser(request):
    room = Room.objects.all()
    users = User.objects.all()
    password = request.POST['password']
    email = request.POST['email']
    entry = User.objects.get(email=email)
    
    if users.filter(pk=entry.pk).exists():
        if entry.password==password:
            return render(request, 'booking/bookingDetail.html',{
            'room': room,'user':entry,
             })
            
        
        
def userAuthView(request):
    return render(request, 'booking/userAuth.html')


class UserView(generics.ListCreateAPIView):
    """
    Returns a list of all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserInstanceView(generics.RetrieveAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingView(generics.ListCreateAPIView):
    model =Booking
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingInstanceView(generics.RetrieveAPIView):
    """
    Returns a single booking.
    Also allows updating and deleting
    """
    queryset = Booking.objects.all()
    model = Booking
    serializer_class = BookingSerializer







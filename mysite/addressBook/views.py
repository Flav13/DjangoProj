from django.shortcuts import render
from rest_framework import generics
from addressBook.serializers import ContactSerializer
from addressBook.models import Contact

# Create your views here.


def index_view(request):
    contacts = Contact.objects.all() 
    return render(request, 'addressBook/index.html',{
            'contacts': contacts,})

class ContactsView(generics.ListCreateAPIView):
    """
    Returns a list of all contatcs.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single contact.
    Also allows updating and deleting
    """
    queryset = Contact.objects.all()
    model = Contact
    serializer_class = ContactSerializer


from django.shortcuts import render
from rest_framework import generics
from bookLib.serializers import AuthorSerializer
from bookLib.models import Author
from django.views.decorators.csrf import csrf_exempt

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'bookLib/index.html', response)


class AuthorView(generics.ListCreateAPIView):
    """
    Returns a list of all authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorInstanceView(generics.RetrieveAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    #queryset = Author.objects.all()
    model = Author
    serializer_class = AuthorSerializer

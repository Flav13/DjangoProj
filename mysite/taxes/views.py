from django.http import HttpResponse
from .models import Client
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from .forms import ClientForm
from django.views import generic
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



class IndexView(FormView):  
    template_name = 'taxes/index.html'
    form_class = ClientForm 
   # return HttpResponseRedirect(reverse('taxes:results'))


class ResultsView(generic.DetailView):
    model=Client
    #response = "You're looking at the results of question"
    template_name='taxes/results.html'

    
def calculate(request):
    
    if validateEmail(request.POST['email']):
        client = Client()
        client.setFirstName(request.POST['firstName'])
        client.setLastName(request.POST['lastName'])
        client.setEmail(request.POST['email'])
        client.setTaxYear(request.POST['taxYear'])
        client.setGrossSalary(request.POST['grossSalary'])
        client.calculateTax()
        client.save()
        # return HttpResponse(client.grossSalary)
        return HttpResponseRedirect(reverse('taxes:results',args=(client.id,)))
    else:
         return render(request, 'taxes/index.html', {
            
            'error_message': "Invalid E-Mail address!!",
             })

    
def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError: 
        return False

# Create your views here.

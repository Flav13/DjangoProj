from django import forms

class ClientForm(forms.Form):  
    firstName= forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    taxYear = forms.CharField(max_length=100)
    grossSalary = forms.CharField(max_length=100)
    
    

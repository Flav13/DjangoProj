from rest_framework import serializers
from addressBook.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','given_name','family_name','email_address','phone_number','street','city','post_code','country')
        

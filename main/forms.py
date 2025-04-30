
from django.forms import ModelForm
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
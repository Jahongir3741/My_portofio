from django.forms import ModelForm
from .models import Contact

class ContactForms(ModelForm):

  class Meta:
    model=Contact
    fields=("your_name","your_email","subject","message",)

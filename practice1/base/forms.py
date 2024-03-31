from django.forms import ModelForm
from .models import *

class studentform(ModelForm):
    class Meta:
        model= Student
        fields= '__all__'
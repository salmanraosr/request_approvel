from django import forms
from .models import Request
#DataFlair
class RequestCreate(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
from django import forms
from .models import TempDelivery

class TempDeliveryForm(forms.ModelForm):
    class Meta:
        model=TempDelivery
        fields=("food_type",)
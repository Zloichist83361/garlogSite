from django import forms
from django.db import models
from django.db.models import fields

from calculator.models import Calculate, Term

class CalculateForm(forms.ModelForm):
    class Meta:
        model = Calculate
        fields = '__all__'



class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = '__all__'
        
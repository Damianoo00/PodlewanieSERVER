from django import forms
from .models import Programator

class ProgramatorForm(forms.ModelForm):
    class Meta:
        model = Programator
        fields = [
            'time_wylewanie',
            'time_I_pole',
            'time_II_pole',
            'time_III_pole'
        ]
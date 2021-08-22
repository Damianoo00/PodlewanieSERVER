from django import forms
from .models import Flow

class FlowForm(forms.ModelForm):
    class Meta:
        model = Flow
        fields = [
            'value'
        ]
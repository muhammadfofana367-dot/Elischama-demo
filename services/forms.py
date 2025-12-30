from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['source_language', 'target_language', 'document']
        widgets = {
            'source_language': forms.TextInput(attrs={'class': 'form-control'}),
            'target_language': forms.TextInput(attrs={'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
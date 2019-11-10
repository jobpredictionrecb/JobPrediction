from django import forms
from .models import Resume_Model


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume_Model
        fields = ['photo']
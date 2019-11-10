from django import forms
from .models import FeedbackModel

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['name','email','feedback']
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Name', 'name': 'Name', 'id': 'common_id_for_imputfields',
                                           'class': 'form-control'}),
            "email": forms.EmailInput(
                attrs={'placeholder': 'description', 'name': 'description', 'id': 'common_id_for_imputfields1',
                       'class': 'form-control'}),
            "feedback": forms.Textarea(
                attrs={'placeholder': 'description', 'name': 'description', 'id': 'common_id_for_imputfields',
                       'class': 'form-control'}),

        }
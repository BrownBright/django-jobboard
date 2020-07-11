from django import forms
from .models import Apply , job


class ApplyForm(forms.ModelForm):
     class Meta:
        model = Apply
        fields = ['name','email','link','cv','cover_letter']

class post_job(forms.ModelForm):
   class Meta:
         model = job
         fields = '__all__'
         exclude = ('slug','owner')

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms

from .models import InternshipPost

class UserCreateForm(UserCreationForm):
	class Meta:
       
		fields = ('username', 'email', 'password1', 'password2')
		model = get_user_model()
      
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['username'].label.widget.attrs.update({'class': 'form-control'})
			self.fields['email'].widget.attrs.update({'class': 'form-control'})

class InternshipPostCreateForm(forms.ModelForm):
	class Meta:
		model = InternshipPost
		fields = [
			'title',
			'last_date',
			'description',
			'registration_link'
		]
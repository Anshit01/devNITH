from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class UserCreateForm(UserCreationForm):
	class Meta:
        # model = Account
		fields = ('username', 'email', 'password1', 'password2','organisation')
		model = get_user_model()
        # model = Account

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['username'].label.widget.attrs.update({'class': 'form-control'})
			self.fields['email'].widget.attrs.update({'class': 'form-control'})
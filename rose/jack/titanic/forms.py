from django import forms
from titanic.models import friends

class friendsForm(forms.ModelForm):
	class Meta:
		model=friends
		fields='__all__'


from django import forms

from .models import Myaddress

# create a ModelForm
class MyaddressForm(forms.ModelForm):
	class Meta:
		model = Myaddress
		fields = ("fname","lname","phone","address","relationship")

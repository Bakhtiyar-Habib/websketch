from django import forms
from .models import Discuss

class DiscussForm(forms.Form):
	name 		= forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}))
	email 		= forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
	phone 		= forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Your Phone Number"}))
	description	= forms.CharField(
						required=False, 
						widget=forms.Textarea({
							"class": "form-control halfwidth1", 
							"placeholder": "Your Description"
							}))
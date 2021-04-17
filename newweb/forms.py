from django import forms
from .models import contact
from .models import careers
from django.forms import ModelForm


class ContactForm(ModelForm):
	class Meta:
		model = contact
		fields = '__all__'
class Careersview(ModelForm):
	class Meta:
		model = careers
		fields = '__all__'
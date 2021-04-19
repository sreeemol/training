from django.shortcuts import render,redirect
from .forms import ContactForm
from .forms import Careersview
from django.http import HttpResponse
from .models import contact

# Create your views here.
def app(request):
    return render(request, 'index.html',{})
def terms(request):
    return render(request, 'terms.html',{})
def careers(request):
	form = Careersview()
	if request.method == 'POST':
		form = Careersview(request.POST)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request,'careers.html',context)
def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request,'contact.html',context)
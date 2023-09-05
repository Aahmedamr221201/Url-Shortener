from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Url
from .forms import UrlForm
import pyshorteners
import urllib
import uuid
import requests
# Create your views here.


def about_page_view(request):
	return render(request,"base.html",{})



def home_page_view(request):
	my_form = UrlForm()
	base_url = "http://127.0.0.1:8000/"
	unique_id=""
	short_url= ""
	if request.method == "POST":
		my_form=UrlForm(request.POST)
		if my_form.is_valid():
			url = my_form.cleaned_data['url']
			unique_id = uuid.uuid4()
			unique_id = str(unique_id)[:7]
			Url.objects.create(original_url = url,unique_id = unique_id)
			short_url = base_url+unique_id
		else:
			print("the data is not valid")	
	context = {
	"form":my_form,
	"short_url":short_url	
	}
	return render(request,"home.html",context)


def redirect_page(request,id):
	obj = get_object_or_404(Url,unique_id = id)
	long_url= obj.original_url
	print("here is the url : " , long_url)
	return redirect(long_url)

from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import RegisterForm

def register(response):
    if response.method == "POST":
    	form = RegisterForm(response.POST)
    	if form.is_valid():
    	    form.save()
    	return redirect("/home")
    else:
	    form = RegisterForm()
    return render(response, "accounts/register.html", {"form":form})

def index(request):
    return render(request, "index.html")

def add_item(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)

def list_items(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)

def view_item(request):
    return HttpResponse("You're voting on question.")

def add_customer(request):
    response = "You're looking at the results of question."
    return HttpResponse(response )

def list_customers(request):
    response = "You're looking at the results of question."
    return HttpResponse(response )

def view_customer(request):
    return HttpResponse("You're voting on question." )

def create_estimate(request):
    return HttpResponse("You're looking at question." )

def list_estimates(request):
    return HttpResponse("You're voting on question." )

def view_estimate(request):
    return HttpResponse("You're voting on question." )

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contact
#from .models import Post
# Create your views here.

def hello(request):
  return HttpResponse("hello!")

def contact(request, id):
  contact = get_object_or_404(Contact, id=id)

  return HttpResponse(contact.name)

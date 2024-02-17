from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import create_user_form
from .models import users

#based on the url chosen, a call to grab the information and send it to you to render as a website will be made

def members(request):
  template = loader.get_template('members.html')
  return HttpResponse(template.render())

#def create(request):
  #form = create_user_form()
  #return render(request, 'create.html', {'form' : form})
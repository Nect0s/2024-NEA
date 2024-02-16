from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import create_user_form
from .models import users

def members(request):
  template = loader.get_template('members.html')
  return HttpResponse(template.render())

def create(request):
  form = create_user_form(request.POST)
  return render(request, 'create.html', {'form' : form})
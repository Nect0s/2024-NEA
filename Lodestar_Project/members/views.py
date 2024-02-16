from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from members.forms import create_user_form
from members.models import users

def members(request):
  template = loader.get_template('members.html')
  return HttpResponse(template.render())

def create_user(request):
  form = create_user_form(request.POST)
  return render(request, 'templates\create.html', {'form' : form})
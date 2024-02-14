from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import CreateUserForm

def members(request):
  template = loader.get_template('members.html')
  return HttpResponse(template.render())


def create_user_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Perform authentication
            # For example:
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
            #     login(request, user)
            #     return redirect('home')  # Redirect to home page after successful login
            # else:
            #     form.add_error(None, "Invalid username or password")
            pass
    else:
        form = CreateUserForm()
    
    return render(request, 'create.html', {'form': form})
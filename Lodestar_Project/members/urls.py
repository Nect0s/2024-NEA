from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members')
    #path('create/', views.create, name='create'),
]

#based on which web page is typed into the search bar, will call a specific "view" to be loaded
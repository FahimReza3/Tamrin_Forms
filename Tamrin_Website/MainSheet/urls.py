from django.urls import path
from . import views


urlpatterns = [
    path('' , views.Main , name="MainSheet"),
    path('AddUser' , views.AddUser , name="AddUser Page")
]
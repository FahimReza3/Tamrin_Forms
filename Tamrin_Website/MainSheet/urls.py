from django.urls import path
from . import views


urlpatterns = [
    path('' , views.Main , name="MainSheet"),
    path('AddUser' , views.AddUser , name="AddUser Page"),
    path('ViewUser' , views.ViewUser , name="ViewUser Page"),
    path('DeletUser/<int:id>' , views.DeletUser , name="DeletUser Page"),
    path('UpdateUser' , views.UpdateUser , name="UpdateUser Page"),
]
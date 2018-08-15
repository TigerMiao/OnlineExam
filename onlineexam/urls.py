from django.urls import path
from onlineexam import views

urlpatterns = [
    path('', views.home_page, name='home'),
]


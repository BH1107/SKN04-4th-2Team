from django.urls import path
from . import views

app_name = 'laptops'

urlpatterns = [
    path('', views.chat_view, name='chat'),
]
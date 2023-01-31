from django.urls import path
from . import views # imports the created view from the same directory

urlpatterns = [
    path("", views.index, name='index'),
    path("andrew", views.andrew, name='andrew'),
    path("parvin", views.parvin, name='parvin'),
]
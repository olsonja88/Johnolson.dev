from django.urls import path
from . import views

urlpatterns = [
    path("", views.gameasset_index, name="gameasset_index")
]

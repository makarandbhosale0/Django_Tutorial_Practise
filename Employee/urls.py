from django.urls import path
from . import views

urlpatterns = [
    path('<int:primary_key>/', views.employe_details)
]
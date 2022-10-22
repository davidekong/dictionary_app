from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.home, name='search')
]

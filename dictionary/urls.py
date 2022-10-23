from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.home, name='search'), 
    path('output/<word>', views.output, name='output')
]

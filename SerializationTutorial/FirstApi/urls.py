from django.urls import path
from django.urls import include
from .views import api_request

urlpatterns = [
    path('get/', api_request, name='get')
]

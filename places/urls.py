from django.urls import path
from django.urls.resolvers import URLPattern
from .views import places

urlpatterns = [
    path('', places, name='places_list')
]
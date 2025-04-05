from django.urls import path
from .views import test_vocacional

urlpatterns = [
    path('', test_vocacional, name='test_vocacional'),
]

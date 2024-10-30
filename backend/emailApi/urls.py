from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Subscribe.as_view(), name='register'),
    path('register/<int:id>/', Subscribe.as_view(), name='register'),
]
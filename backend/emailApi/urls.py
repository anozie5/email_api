from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', Subscribe.as_view(), name='register'),
    path('register/<int:id>/', Subscribe.as_view(), name='register'),
]


# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'register', Subscribe)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
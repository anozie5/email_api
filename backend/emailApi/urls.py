from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', Subscribe.as_view(), name='register'),
    path('register/<int:id>/', Subscribe.as_view(), name='register'),
    path('signup/', PrivateSignUpView.as_view()),
    path('login/', PrivateLoginView.as_view()),
]
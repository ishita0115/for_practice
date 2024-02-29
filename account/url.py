
from django.urls import path
from account.views import userRegistrationView,UserLoginView
urlpatterns = [
    path('register/',userRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
]

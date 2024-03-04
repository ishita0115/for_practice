
from django.urls import path
from account.views import userRegistrationView,UserLoginView,UserProfileView,ChangePasswordView,HouseListCreateView
urlpatterns = [
    path('register/',userRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('changepass/',ChangePasswordView.as_view(),name='changepass'),
    path('houses/', HouseListCreateView.as_view(), name='house-list-create'),
    
]

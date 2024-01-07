from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.RegisterUser.as_view(), name='reg'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('profile/<int:user_pk>', views.ProfileUser.as_view(), name='profile'),
    path('update_profile/<int:user_pk>', views.UpdateUserProfile.as_view(), name='update_profile'),
    path('update_profile/<int:user_pk>/', views.UpdateUserProfile.as_view(), name='update_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
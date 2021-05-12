from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.signup_view, name="account-signup"),
    path('login/', views.login_view, name="account-login"),
    path('log-out/', views.logout_view, name="account-logout"),
    path('user/profile/', views.profile_view, name="account-profile"),
    
    path('reset-password/', 
        auth_views.PasswordResetView.as_view(template_name = "accounts/reset_password.html"), 
        name ='reset_password'),
    
    path('reset-password-sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), 
        name ='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_change.html"), 
        name ='password_reset_confirm'),
    
    path('reset-password-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"), 
        name ='password_reset_complete'),
]

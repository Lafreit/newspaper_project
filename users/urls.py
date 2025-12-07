from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    # SIGNUP
    path('signup/', SignUpView.as_view(), name='signup'),

    # LOGIN
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

    # LOGOUT
    path('logout/', LogoutView.as_view(), name='logout'),

    # PASSWORD CHANGE
    path('password_change/',
         PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password_change'),

    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    # PASSWORD RESET
    path('password_reset/',
         PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),

    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
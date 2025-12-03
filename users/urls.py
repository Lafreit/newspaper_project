from django.urls import path
form .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
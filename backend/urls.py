from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('admin/', admin.site.urls),
]

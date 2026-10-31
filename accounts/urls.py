from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'

from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'

# Строго urlpatterns, это зарезервированное слово фреймворка
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('', include('django.contrib.auth.urls')),
]
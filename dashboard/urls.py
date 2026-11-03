from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('users/', views.users_list, name='users_list'),
    path(
        'users/<int:user_id>/toggle-status/',
        views.toggle_user_status,
        name='toggle_user_status'
    ),

    path(
        'users/<int:user_id>/toggle-role/',
        views.toggle_user_role,
        name='toggle_user_role'
    ),
    path('purchases/', views.purchases_list, name='purchases_list'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('work', views.work, name='work'),
    path('user', views.user, name='user'),
    path('client_exists', views.client_exists, name='client_exists'),
    path('client', views.client, name='client'),
    path('success_client/', views.create_client, name='create_client'),
    path('docks_list/', views.docks_list, name='list_docks'),
    # path('users', views.index, name='users'),
    # path('login_page/', views.login_user, name='main'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
    path('user_details/<int:user_id>/', views.user_details, name='user-details'),
    path('client_details/<int:client_id>/', views.client_details, name='client-details'),
]

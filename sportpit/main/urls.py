
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    # path('login_page/', views.login_user, name='main'),
    # path('logout/', views.logout_user)
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('dashboard/', views.main_page, name='main_page'),
    path('go/<slug:slug>/', views.tracking_view, name='tracking_view'),
    path('public_page/', views.public_page, name='public_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

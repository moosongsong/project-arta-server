from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_us),
    path('login/', views.login),
    path('mypage/', views.mypage),
    path('', views.landing),
]

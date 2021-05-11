from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ExhibitionList.as_view()),
    path('', views.SinglePage.landing_page),
    path('about/', views.SinglePage.about_page),
    path('exhibition/', views.ExhibitionPage.exhibition_list_page),
    path('exhibition/about/<int:pk>/', views.SinglePage.about_page),
    path('exhibition/<int:pk>/', views.ExhibitionPage.exhibition_detail_page),

]
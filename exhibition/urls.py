from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ExhibitionList.as_view()),
    path('', views.SinglePage.landing_page),
    path('about/', views.SinglePage.about_page),
    path('preference/', views.LikePage.all_like_page),
    path('search/', views.SearchPage.search_page),
    path('search/<str:key>/', views.SearchPage.search_result_page),

    path('exhibition/', views.ExhibitionPage.exhibition_list_page),
    path('exhibition/<int:pk>/', views.ExhibitionPage.exhibition_detail_page),
    path('exhibition/gueskbook/<int:pk>/', views.ExhibitionPage.exhibition_detail_page),
    path('exhibition/about/<int:pk>/', views.SinglePage.about_page),

    path('exhibition/piece/<int:pk>/', views.ExhibitionPage.exhibition_detail_page),
    path('exhibition/piece/comment/<int:pk>/', views.ExhibitionPage.exhibition_detail_page),
]

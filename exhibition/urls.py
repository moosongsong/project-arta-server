from django.urls import path
from . import views

urlpatterns = [
    path('', views.SinglePage.landing_page),
    path('about/', views.SinglePage.about_page),
    path('login/', views.SinglePage.login_page),
    path('test/', views.SinglePage.test_page),

    path('preference/', views.LikePieceList.as_view()),
    path('preference/piece/', views.LikePieceList.as_view()),
    path('preference/exhibition/', views.LikeExhibitionList.as_view()),
    path('search/', views.SearchPage.search_page),
    # path('search/result/all/<str:q>/', views.PieceSearch.as_view()),
    path('search/result/piece/<str:q>/', views.PieceSearch.as_view()),
    path('search/result/exhibition/<str:q>/', views.ExhibitionSearch.as_view()),

    path('exhibition/', views.ExhibitionList.as_view()),
    # path('exhibition/<int:pk>/', views.ExhibitionDetail.as_view()),
    path('exhibition/<int:pk>/', views.PieceList.as_view()),
    path('exhibition/<int:pk>/new_guestbook/', views.GuestbookManage.new_guestbook),
    path('exhibition/delete_guestbook/<int:pk>/', views.GuestbookManage.delete_guestbook),
    path('exhibition/<int:pk>/new_like/', views.LikeManage.exhibition_like),
    path('exhibition/<int:pk>/dislike/', views.LikeManage.exhibition_dislike),

    path('exhibition/piece/<int:pk>/', views.PieceDetail.as_view()),
    # path('exhibition/piece/<int:pk>/', views.PieceManage.show_piece_detail),
    path('exhibition/piece/<int:pk>/new_comment/', views.CommentManage.new_comment),
    path('exhibition/piece/delete_comment/<int:pk>/', views.CommentManage.delete_comment),
    path('exhibition/piece/<int:pk>/new_like/', views.LikeManage.piece_like),
    path('exhibition/piece/<int:pk>/dislike/', views.LikeManage.piece_dislike),

]

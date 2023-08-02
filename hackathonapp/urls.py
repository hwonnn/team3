from django.urls import path, include
from . import views



urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:post_id>/comment/', views.CommentList.as_view()),
    path('posts/<int:post_id>/comment/<int:pk>/', views.CommentDetailList.as_view()),
    #path('posts/<int:post_id>/comment/<int:comment_id>/like/', views.CommentLike.as_view()),
]
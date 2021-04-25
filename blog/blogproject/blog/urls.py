from django.urls import path
from .views import (
    BlogListView, 
    detail_view, 
    BlogCreateView, 
    BlogUpdateView,
    BlogDeleteView,
    CommentUpdateView,
    CommentDeleteView,
)


urlpatterns = [
    path('', BlogListView.as_view(), name="post-list"),
    path('<int:pk>/', detail_view, name="post-detail"),
    path('post/new/', BlogCreateView.as_view(), name="new-post"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name="edit-post"),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="delete-post"),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name="edit-comment"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="delete-comment"),  
]
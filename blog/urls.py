from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create_post/', views.AddPost.as_view(), name='create_post'),
    path('comment:<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('update_comment/<int:pk>/', views.UpdateComment.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:slug>/', views.TagListView.as_view(), name='tag_list'),
    path('update_post/<slug:post_slug>', views.UpdatePost.as_view(), name='update_post'),
    path('delete_post/<slug:post_slug>', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:slug>/<slug:post_slug>', views.PostDetailView.as_view(), name='post_single'),
   # path('', cache_page(60*15)(views.HomeView.as_view()), name='home'),

]
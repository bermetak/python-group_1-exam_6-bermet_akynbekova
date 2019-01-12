from django.urls import path
from webapp.views import PostListView, UserListView, UserDetailView, PostDetailView, PostCreateView, \
    PostEditView, PostDeleteView


app_name = 'webapp'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('user', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]
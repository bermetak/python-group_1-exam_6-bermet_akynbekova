from django.urls import path
from webapp.views import PostListView, UserListView, UserDetailView, PostDetailView


app_name = 'webapp'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('user', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]
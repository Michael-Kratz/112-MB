from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="posts"),
    path('detail/', PostDetailView.as_view(), name="detail"),
    
]
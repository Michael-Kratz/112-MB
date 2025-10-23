from django.urls import path
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="posts"),
    path('detail/', PostListView.as_view(), name="detail"),
    
]
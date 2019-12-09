from django.urls import path
from .views import  index, PostDetailView, CreatePostView

urlpatterns = [

    path('', index.as_view(), name='index'),
    path('article/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('article/new/', CreatePostView.as_view(), name='post-new'),
]

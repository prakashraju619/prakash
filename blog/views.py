from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
class index(ListView):
	model = Post
	template_name = 'blog/index.html'


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class CreatePostView(CreateView):
	model = Post
	template_name = 'blog/add_post.html'
	fields = '__all__'

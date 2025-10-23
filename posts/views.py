from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostListView(ListView):
    """
    PostListView is going to retrieve all of the objects from the Post table in the db
    """

    # template_name attribute is going to render an specific html file
    template_name = "posts/list.html"
    # model attribute is to let know django which model we want to retrieve data
    model = Post
    # context_object_name would allows to modify the name on how we call it inside of the htmls
    context_object_name = "posts"


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "detailed"

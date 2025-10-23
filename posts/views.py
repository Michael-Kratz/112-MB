from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy


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
    """
    PostDetailView Class is going to retriews a simple element from the Post table in the db
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "detailed"

class PostCreateView(CreateView):
    """
    PostCreateView Class help us to create a new post object
    """
    template_name ="posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        print(form)
        print(User.objects.all())
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    """
    PostUpdateView Class allow us to edit existing records from the db
    """
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    """
    PostDeleteView Class allow us to delete an existing record from the db
    """
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("posts_list")

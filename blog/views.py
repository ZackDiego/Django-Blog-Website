from django.shortcuts import render, get_object_or_404 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<view_type>.html
    context_object_name = 'posts' 
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User,  username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date')

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields=['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields=['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

def about(request):
    return render(request, 'blog/about.html', {"title": "about"})

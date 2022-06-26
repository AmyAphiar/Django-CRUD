from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from blog.models import Post

class PostListView(ListView):
    model = Post
    template = 'blog/post_list.html'

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
    template = 'blog/post_form.html'

class PostDetailView(DetailView):
    model = Post
    template = 'blog/post_detail'

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
    template = 'blog/post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
    template = 'blog/post_confirm_delete.html'
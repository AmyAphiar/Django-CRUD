from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from blog.models import Post

def PostListView(request):
    return HttpResponse()

def PostCreateView(request):
    template = loader.get_template('post_create.html')
    return HttpResponse(template.render({}, request))




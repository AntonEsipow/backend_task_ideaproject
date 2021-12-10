from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Image


class ImageListView(ListView):
    model = Image
    context_object_name = 'image_list'
    template_name = 'home.html'


class CreateImageView(CreateView):
    model = Image
    form_class = PostForm
    template_name = 'image/image_add.html'
    success_url = reverse_lazy('home')


class ImageDetailView(DetailView):
    model = Image
    context_object_name = 'image'
    template_name = 'image/image_detail.html'
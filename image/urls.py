from django.urls import path
from .views import ImageListView, CreateImageView, ImageDetailView

urlpatterns = [
    path('site_media/', ImageListView.as_view(), name='home'),
    path('site_media/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('create/', CreateImageView.as_view(), name='add_image'),
]
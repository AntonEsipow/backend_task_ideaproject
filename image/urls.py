from django.urls import path
from .views import ImageListView, CreateImageView, ImageDetailView

urlpatterns = [
    path('', ImageListView.as_view(), name='home'),
    path('<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('create/', CreateImageView.as_view(), name='add_image'),
]
from django.urls import path
from .views import ImageListApiView, ImageDetailApiView

urlpatterns = [
    path('images/', ImageListApiView.as_view(), name='list_api'),
    path('images/<int:pk>/', ImageDetailApiView.as_view(), name='detail_api'),
]
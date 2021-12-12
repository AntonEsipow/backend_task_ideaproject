from rest_framework import generics, permissions
from image.models import Image
from .serializers import ImageSerializer


class ImageListApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
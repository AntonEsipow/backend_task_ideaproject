from rest_framework import serializers
from django.contrib.auth.models import User
from image.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['id', 'title', 'image',]
from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from PIL import Image
from io import BytesIO

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
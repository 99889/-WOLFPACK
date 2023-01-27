from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import CustomUser
from .models import CustomUser
from .serializers import CustomUserSerializer, ImageSerializer
    
from rest_framework.views import APIView, ViewSet
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from PIL import Image, ImageOps
from io import BytesIO
from .serializers import ImageSerializer

class ImageViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = Image.open(BytesIO(request.data['image'].read()))
            # Create Thumbnail
            image.thumbnail((200, 300))
            image_io = BytesIO()
            image.save(image_io, format='JPEG')
            image_io.seek(0)
            # Create Medium
            image = Image.open(BytesIO(request.data['image'].read()))
            image = image.resize((500, 500))
            image_io = BytesIO()
            image.save(image_io, format='JPEG')
            image_io.seek(0)
            # Create Large
            image = Image.open(BytesIO(request.data['image'].read()))
            image = image.resize((1024, 768))
            image_io = BytesIO()
            image.save(image_io, format='JPEG')
            image_io.seek(0)
            # Create Grayscale
            image = Image.open(BytesIO(request.data['image'].read()))
            image = ImageOps.grayscale(image)
            image_io = BytesIO()
            image.save(image_io, format='JPEG')
            image_io.seek(0)
            return Response({"thumbnail": image_io.getvalue(), "medium": image_io.getvalue(), "large": image_io.getvalue(), "grayscale": image_io.getvalue()})
        else:
            return Response(serializer.errors)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_class = (JSONWebTokenAuthentication,)
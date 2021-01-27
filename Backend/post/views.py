from .serializers import RegistrationSerializer, RegistrationAdminSerializer
from .models import Registration, RegistrationAdmin
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict

class PublicRigisterView(APIView):
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request):
        print(request.data)
        posts_serializer = RegistrationSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            # print(posts_serializer.data)
            return Response(posts_serializer.data,status=status.HTTP_201_CREATED)
        else:
            # print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicLoginView(APIView):
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        try:
            go = Registration.objects.filter(email=data['email'], password=data['password']).values().first()            
        except Registration.DoesNotExist:
            go = None
        if go:
            dict_obj = go #{"success"}
            # del dict_obj['new_upload']
            # del dict_obj['used_upload']
        else:
            dict_obj = {'not matched'}
        return Response(dict_obj)

class AdminRegisterView(APIView):
    parser_classes = (FormParser, MultiPartParser)
    def post(self, request):
        posts_serializer = RegistrationAdminSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            print(posts_serializer.data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminLoginView(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data)
        data = request.data
        try:
            go = RegistrationAdmin.objects.filter(email=data['email'], password=data['password'])            
        except RegistrationAdmin.DoesNotExist:
            go = None
        if go:
            dict_obj = {"scuccess"}
        else:
            dict_obj = {'not matched'}
        return Response(dict_obj)
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer


class Register(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('email',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_401_UNAUTHORIZED)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

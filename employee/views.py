from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeRegisterSerializer


class EmployeeList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    # get method handler
    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeRegisterSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('branch', 'empID',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeDetails(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    # get method handler
    queryset = Employee.objects.all()
    serializer_class = EmployeeRegisterSerializer

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)

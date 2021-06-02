from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Attendance
from .serializers import AttendanceSerializer, FetchAttendanceSerializer


class FetchAttendance(generics.ListCreateAPIView):
    queryset = Attendance.objects.select_related('empID')

    print(str(queryset.query))
    serializer_class = FetchAttendanceSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(queryset)
        return obj


class AttendanceInput(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    # get method handler
    queryset = Attendance.objects.all().order_by("id")
    serializer_class = AttendanceSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('empID', 'daydate',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AttendanceList(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    # get method handler
    queryset = Attendance.objects.all().order_by("id")
    serializer_class = AttendanceSerializer

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)

from django.db.models import Q  # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Attendance
from employee.serializers import EmployeeRegisterSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    # timing_in = serializers.TimeField(
    #     format='%H:%M:%S', input_formats="%H:%M:%S")
    # timing_out = serializers.TimeField(
    #     format='%H:%M:%S', input_formats="%H:%M:%S", required=False)

    class Meta:
        model = Attendance
        fields = ['id', 'empID', 'daydate',
                  'timing_in', 'timing_out', 'status']


class FetchAttendanceSerializer(serializers.ModelSerializer):
    empData = EmployeeRegisterSerializer(source="empID")

    class Meta:
        model = Attendance
        fields = ['id', 'empData', 'empID', 'daydate',
                  'timing_in', 'timing_out', 'status']

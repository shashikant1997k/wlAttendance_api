from django.db.models import Q  # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Employee


class EmployeeRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'empID', 'name', 'aadharNumber', 'aadharFrontImage', 'aadharBackImage',
                  'pancard', 'pancardImage', 'email', 'mobile', 'branch', 'address', 'role', 'date_joined', 'dob', 'profileImage', 'isActive', 'bankname', 'accountNumber', 'IFSCCode', 'passbookImage']

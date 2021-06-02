from django.db.models import Q  # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.core.exceptions import ValidationError
from uuid import uuid4
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'accessToken']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            validated_data['password'] = make_password(
                validated_data['password'])
            return super(UserSerializer, self).create(validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    email = serializers.CharField()
    password = serializers.CharField()
    accessToken = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        email = data.get("email", None)
        password = data.get("password", None)
        if not email and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in email:
            user = User.objects.filter(
                Q(email=email) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError(
                    {"message": "User credentials are not correct.", "code": "401"})
            user = User.objects.get(email=email)
        else:
            user = User.objects.filter(
                Q(username=email) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError(
                    {"message": "User credentials are not correct.", "code": "401"})
            user = User.objects.get(username=email)
        if user.ifLogged:
            raise ValidationError(
                {"message": "User already logged in.", "code": "203"})
        user.ifLogged = True
        data['accessToken'] = uuid4()
        user.accessToken = data['accessToken']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'accessToken',
        )

        read_only_fields = (
            'accessToken',
        )


class UserLogoutSerializer(serializers.ModelSerializer):
    accessToken = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        accessToken = data.get("accessToken", None)
        print(accessToken)
        user = None
        try:
            user = User.objects.get(accessToken=accessToken)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.accessToken = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'accessToken',
            'status',
        )

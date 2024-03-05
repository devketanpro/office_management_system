from rest_framework import serializers

from users.models import Worker, User, USER_TYPE


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone", "password", "first_name", "last_name")
        extra_kwargs = {
            "email": {"required": True, "allow_blank": False},
            "phone": {"required": True, "allow_blank": False},
            "password": {"required": True, "allow_blank": False},
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
        }

    def validate_email(self , value):
        user = User.objects.filter(email=value.lower())
        if user:
            raise serializers.ValidationError("User with this email address already exists")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data,
            role=USER_TYPE.USER
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone", "password", "first_name", "last_name", "role")


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
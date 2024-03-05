from rest_framework import serializers

from users.models import Worker, User, USER_TYPE


class SignUpSerializer(serializers.ModelSerializer):
    """
    Serializer for user sign up.
    This serializer is used to create new User instances during the sign-up process.
    """

    class Meta:
        """
        Meta class for SignUpSerializer.
        Specifies the model, fields, and extra kwargs for serialization.
        """
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
        """
        Validate email uniqueness.
        Checks if the email address is already registered.
        """
        user = User.objects.filter(email=value.lower())
        if user:
            raise serializers.ValidationError("User with this email address already exists")
        return value

    def create(self, validated_data):
        """
        Create a new user.
        Creates a new User instance with the provided validated data.
        """
        user = User.objects.create_user(
            **validated_data,
            role=USER_TYPE.USER
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    This serializer is used to serialize/deserialize User instances.
    """
    class Meta:
        """
        Meta class for UserSerializer.
        Specifies the model and fields for serialization.
        """
        model = User
        fields = ("id", "email", "phone", "password", "first_name", "last_name", "role")


class WorkerSerializer(serializers.ModelSerializer):
    """
    Serializer for Worker model.
    This serializer is used to serialize/deserialize Worker instances.
    """
    class Meta:
        """
        Meta class for WorkerSerializer.
        Specifies the model and fields for serialization.
        """
        model = Worker
        fields = "__all__"
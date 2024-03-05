from rest_framework import serializers

from offices.models import Assignment, Office, UserOffice, UserRequest


class OfficeSerializer(serializers.ModelSerializer):
    """
    Serializer for Office model.
    This serializer is used to serialize/deserialize Office instances.
    """

    class Meta:
        model = Office
        fields = "__all__"


class UserOfficeSerializer(serializers.ModelSerializer):
    """
    Serializer for UserOffice model.
    This serializer is used to serialize/deserialize UserOffice instances.
    """
    class Meta:
        model = UserOffice
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Assignment model.

    This serializer is used to serialize/deserialize Assignment instances.
    It includes a custom field 'worker_name' to provide a formatted representation
    of the worker's name.
    """

    worker_name = serializers.SerializerMethodField()
    class Meta:
        model = Assignment
        fields = ('id', 'priority', 'status', 'worker', 'worker_name')
    
    def get_worker_name(self, obj):
        """
        Method to retrieve the formatted representation of the worker's name.
        """

        if obj.worker:
            return obj.worker.user.first_name + " " + obj.worker.user.last_name 
        return None


class UserRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for UserRequest model.

    This serializer is used to serialize/deserialize UserRequest instances.
    It includes the AssignmentSerializer for the 'assignment' field and ensures
    that the 'submitted_by' field corresponds to a valid office for the requesting user.
    """

    assignment = AssignmentSerializer(required=False)
    submitted_by = serializers.PrimaryKeyRelatedField(
        queryset=UserOffice.objects.all()
    )

    class Meta:
        """
        Meta class for UserRequestSerializer.
        Specifies the model, fields, and additional configurations for serialization.
        """
        model = UserRequest
        fields = ('id', 'submitted_by', 'is_active', 'is_deleted',
                   'created', 'request_type', 'title', 'preferred_timeframe',
                   'assignment')

    def validate_submitted_by(self, value):
        """
        Custom validation method for submitted_by field.
        Ensures that the submitted office is valid for the requesting user.
        """
        user = self.context['request'].user
        if value.user != user:
            raise serializers.ValidationError("This is not a valid office for you.")
        return value

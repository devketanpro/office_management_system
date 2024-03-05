from rest_framework import serializers

from offices.models import Assignment, Office, UserOffice, UserRequest


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"


class UserOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOffice
        fields = "__all__"


class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('priority', 'status', 'worker')


class UserRequestSerializer(serializers.ModelSerializer):
    assignment = AssignmentListSerializer(required=False)
    submitted_by = serializers.PrimaryKeyRelatedField(
        queryset=UserOffice.objects.all()
    )

    class Meta:
        model = UserRequest
        fields = ('id', 'submitted_by', 'is_active', 'is_deleted',
                   'created', 'request_type', 'title', 'preferred_timeframe',
                   'assignment')

    def validate_submitted_by(self, value):
        user = self.context['request'].user
        if value.user != user:
            raise serializers.ValidationError("This is not a valid office for you.")
        return value

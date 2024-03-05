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


class AssignmentSerializer(serializers.ModelSerializer):
    worker_name = serializers.SerializerMethodField()
    class Meta:
        model = Assignment
        fields = ('id', 'priority', 'status', 'worker', 'worker_name')
    
    def get_worker_name(self, obj):
        if obj.worker:
            return obj.worker.user.first_name + " " + obj.worker.user.last_name 
        return None


class UserRequestSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(required=False)
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

from rest_framework import serializers

from offices.models import Office, UserOffice, UserRequest


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"


class UserOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOffice
        fields = "__all__"


class UserRequestSerializer(serializers.ModelSerializer):
    submitted_by = serializers.PrimaryKeyRelatedField(queryset=UserOffice.objects.all())

    class Meta:
        model = UserRequest
        fields = '__all__'

    def validate_submitted_by(self, value):
        user = self.context['request'].user
        if value.user != user:
            raise serializers.ValidationError("This is not a valid office for you.")
        return value

from rest_framework import serializers

from offices.models import Office, UserOffice


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"


class UserOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOffice
        fields = "__all__"
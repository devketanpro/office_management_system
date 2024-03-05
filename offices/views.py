from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from users.permissions import AdminPermission
from offices.models import Office, UserOffice
from offices.serializers import OfficeSerializer, UserOfficeSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    __doc__ = """
    A viewset that provides the office data
    """

    permission_classes = [AdminPermission]
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    pagination_class = PageNumberPagination


class UserOfficeViewSet(viewsets.ModelViewSet):
    __doc__ = """
    A viewset that provides the user office data
    """

    permission_classes = [AdminPermission]
    queryset = UserOffice.objects.all()
    serializer_class = UserOfficeSerializer
    pagination_class = PageNumberPagination

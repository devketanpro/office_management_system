from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from users.permissions import AdminPermission
from offices.models import Office
from offices.serializers import OfficeSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    __doc__ = """
    A viewset that provides the office data
    """

    permission_classes = [AdminPermission]
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    pagination_class = PageNumberPagination

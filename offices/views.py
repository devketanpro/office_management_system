from rest_framework import generics, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



from users.permissions import AdminPermission
from users.models import USER_TYPE
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


class GetUserOfficeView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserOfficeSerializer
    pagination_class = PageNumberPagination

    __doc__ = """
        This API is designed to exclusively return the list of currently requested user offices.
    """

    def get(self, request, *args, **kwargs):
        user_office = UserOffice.objects.filter(
            user = request.user
        )
        serializer = self.serializer_class(user_office, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
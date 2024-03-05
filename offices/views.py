from rest_framework import generics, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import USER_TYPE



from users.permissions import AdminPermission, UserPermission
from offices.models import Assignment, Office, UserOffice, UserRequest
from offices.serializers import (
    OfficeSerializer, 
    UserOfficeSerializer,
    UserRequestSerializer,
    AssignmentSerializer,
)


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
    __doc__ = """
        This API is designed to exclusively return the list of currently requested user offices.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserOfficeSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        user_office = UserOffice.objects.none()
        if request.user.role == USER_TYPE.ADMIN:
            user_office = UserOffice.objects.filter(
                user = request.user
            )
        if request.user.role == USER_TYPE.USER:
            user_office = UserOffice.objects.filter(
                user = request.user
            )
        serializer = self.serializer_class(user_office, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RaiseRequestView(generics.CreateAPIView):
    __doc__ = """
            This API is used to raise request by the user.
    """
    serializer_class = UserRequestSerializer
    permission_classes = [UserPermission]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetRequestInfoView(generics.ListAPIView):
    __doc__ = """
        This API is designed to exclusively return the list of currently requested user offices.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserRequestSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        user_office = UserRequest.objects.all()
        if request.user.role == USER_TYPE.ADMIN:
            pass
        if request.user.role == USER_TYPE.USER:
            user_office = user_office.filter(
                submitted_by__user = request.user
            )
        if request.user.role == USER_TYPE.WORKER:
            user_office = user_office.filter(
                assignment__worker = request.user
            )
        serializer = self.serializer_class(user_office, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ManageAssignmentView(generics.UpdateAPIView):
    __doc__ = """
        This API handle assignment like assign worker, \
        change status and update priority.
    """
    permission_classes = [AdminPermission]
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = 'pk'
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from users.models import User, Worker
from users.serializers import WorkerSerializer, UserSerializer, SignUpSerializer
from .utils import get_user_token
from users.permissions import AdminPermission

class SignUpApiView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    __doc__ = """
                SignUp Api view this api is used to create the user
                params:
                   email: EmailField
                   phone: CharField
                   password: CharField
                   first_name: CharField
                   last_name: CharField
                   role: Charfield
            """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_data = get_user_token(request)
            response_status = status.HTTP_201_CREATED
        else:
            response_data = {"message": "Unable to create user"}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(response_data, status=response_status)


class UserViewSet(viewsets.ModelViewSet):
    __doc__ = """
    A viewset that provides the user actions
    """
    permission_classes = [AdminPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination


class WorkerViewSet(viewsets.ModelViewSet):
    __doc__ = """
    A viewset that provides the user actions
    """
    permission_classes = [AdminPermission]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    pagination_class = PageNumberPagination
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet, WorkerViewSet, SignUpApiView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'workers', WorkerViewSet, basename='worker')

urlpatterns =[
    path("sign-up/", SignUpApiView.as_view(), name="signup"),
]
# Generate token
token_urls = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
urlpatterns += token_urls


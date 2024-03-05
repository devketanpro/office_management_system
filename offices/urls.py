from django.urls import path
from rest_framework.routers import DefaultRouter

from offices.views import OfficeViewSet, UserOfficeViewSet, GetUserOfficeView, RaiseRequestView

router = DefaultRouter()
router.register(r'offices', OfficeViewSet, basename='office')
router.register(r'user-office', UserOfficeViewSet, basename='user_office')

urlpatterns = [
    path("user-office-list/", GetUserOfficeView.as_view(), name = "user_office_list"),
    path('raise-request/', RaiseRequestView.as_view(), name='raise_request'),
]

urlpatterns += router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter

from offices.views import (
    OfficeViewSet, 
    UserOfficeViewSet, 
    GetUserOfficeView, 
    RaiseRequestView,
    GetRequestInfoView,
    ManageAssignmentView,
    )

router = DefaultRouter()
router.register(r'offices', OfficeViewSet, basename='office')
router.register(r'user-office', UserOfficeViewSet, basename='user_office')

urlpatterns = [
    path("user-office-list/", GetUserOfficeView.as_view(), name = "user_office_list"),
    path('raise-request/', RaiseRequestView.as_view(), name='raise_request'),
    path('track-request/', GetRequestInfoView.as_view(), name='track_request'),
    path('manage-assignment/<str:pk>/', ManageAssignmentView.as_view(), name='manage_assignment'),
]

urlpatterns += router.urls

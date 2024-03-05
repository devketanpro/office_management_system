from rest_framework.routers import DefaultRouter

from offices.views import OfficeViewSet, UserOfficeViewSet

router = DefaultRouter()
router.register(r'offices', OfficeViewSet, basename='office')
router.register(r'user-office', UserOfficeViewSet, basename='user_office')


urlpatterns = router.urls

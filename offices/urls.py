from rest_framework.routers import DefaultRouter

from offices.views import OfficeViewSet

router = DefaultRouter()
router.register(r'offices', OfficeViewSet, basename='office')

urlpatterns = router.urls

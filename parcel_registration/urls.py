from rest_framework.routers import DefaultRouter

from parcel_registration.views import LetterViewSet, ParcelViewSet

router = DefaultRouter()
router.register(r'letters', LetterViewSet)
router.register(r'parcels', ParcelViewSet)

urlpatterns = router.urls

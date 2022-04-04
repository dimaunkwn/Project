from rest_framework.routers import DefaultRouter

from authentication.views import AuthViewSet

router = DefaultRouter()

router.register('', AuthViewSet, basename='auth')

urlpatterns = [
    *router.urls
]

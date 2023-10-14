from django.urls import include, path
from rest_framework.routers import SimpleRouter

from products.api.views import ProductViewSet

router = SimpleRouter()
router.register("", ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

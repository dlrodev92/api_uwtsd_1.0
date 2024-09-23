from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReferenceViewSet

router = DefaultRouter()

router.register(r'references', ReferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

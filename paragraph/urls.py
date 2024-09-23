from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParagraphViewSet

router = DefaultRouter()
router.register(r'paragraphs', ParagraphViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include
from .views import *
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import viewsets, routers

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'magazines', MagazineViewSet)
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
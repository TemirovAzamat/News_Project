from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="My documentation",
      default_version='alpha-0.0.1',
      description="This is API for news",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="azamatt04@mail.ru"),
      license=openapi.License(name="American License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

swagger_urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('api/', include('news.urls')),
] + swagger_urlpatterns

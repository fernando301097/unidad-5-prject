"""principal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny

from pagos2.v1 import urls as v1_urls
from pagos2.v2 import urls as v2_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "pagos Api",
        default_version = "v2",
        description = "api de pagos",
        terms_of_service = "https://www.google.com/policies/terms/",
        contact = openapi.Contact(email="anred123456@gmail.com"),
        license = openapi.License(name="BSD Licence"),
        ),
    public=True,
    permission_classes=[AllowAny]
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagos.urls')),

    path('v1/', include(v1_urls)),
    path('v2/', include(v2_urls)),

    path('users/', include('users.urls')),

    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
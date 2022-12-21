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
from django.urls import path, include
#from pagos2.v1 import urls as version1
#from pagos2.v2 import urls as version2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagos.urls')),
    #path('v1/', include(version1)),
    #path('v2/', include(version2)),

    path('users/', include('users.urls')),
]
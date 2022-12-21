from rest_framework.routers import DefaultRouter
from .api import PagosView

route = DefaultRouter()
route.register("pagoss", PagosView(), basename="pagoss")

urlpatterns = route.urls
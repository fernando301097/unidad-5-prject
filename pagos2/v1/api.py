from pagos.models import Pagos
from rest_framework.viewsets import ModelViewSet
from .serializers import PagosSerializer
from rest_framework import status, filters
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from .pagination import PagosPagination

class PagosView(ModelViewSet):
    queryset =Pagos.objects.all()
    serializer_class = PagosSerializer


    pagination_class = PagosPagination
    permission_classes = [AllowAny]

    filter_backends = [filters.SearchFilter]
    search_fields = ['usuario__id', 'fecha_pago', 'servicio']

    throttle_scope = 'get'






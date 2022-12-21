from .serializers import ServicesSerializers, Payment_userSerializers, Expired_paymentsSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, filters
from rest_framework.response import Response
from .models import Services, Payment_user, Expired_payments
from .pagination import PagosPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

class ServicesView(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    
    http_method_names = ['get']

    permission_classes = [AllowAny]
    throttle_scope = 'services'

class PaymentUsersView(ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = Payment_userSerializers

    pagination_class = PagosPagination
    filter_backends = [filters.SearchFilter]

    search_fields = ['payment_date', 'expiration_date']
    permission_classes = [AllowAny]

    throttle_scope = 'pagos'
    
class ExpiredPaymentView(ModelViewSet):
    queryset = ExpiredPayments.objects.all()

    serializer_class = Expired_paymentsSerializers
    pagination_class = PagosPagination

    http_method_names = ['get','post']
    permission_classes = [AllowAny]

    throttle_scope = 'expired'

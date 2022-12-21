from rest_framework.routers import DefaultRouter
from .api import ServicesView ,ExpiredPaymentView, PaymentUsersView 

route =DefaultRouter()
route.register("services", ServicesView, basename="services")
route.register("paymentusers", PaymentUsersView, basename="paymentusers")
route.register("expiredpayment", ExpiredPaymentView, basename="expiredpayment")

urlpatterns = route.urls
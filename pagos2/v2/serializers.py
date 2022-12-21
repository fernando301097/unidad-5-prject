from pagos2 import models
from rest_framework.serializers import ModelSerializer

class ServicesSerializers(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class Payment_userSerializers(ModelSerializer):
    class Meta:
        model = Payment_user
        fields = "__all__"

class Expired_paymentsSerializers(ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = "__all__"
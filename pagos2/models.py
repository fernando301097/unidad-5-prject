from django.db import models
from users.models import User

class Services(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)



class Payment_user(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateField(auto_now_add=True)
    expiration_date= models.DateField()

class Expired_payments(models.Model):
    
    payment_user_id = models.ForeignKey(Payment_user, on_delete = models.CASCADE)
    penalty_fee_amount = models.CharField(max_length=100)

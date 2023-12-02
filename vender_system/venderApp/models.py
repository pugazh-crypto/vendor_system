from django.db import models

# Create your models here.
class vender_model(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vender_code = models.CharField(max_length=20)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    fulfillment_rate = models.FloatField()

class purchase_order(models.Model):
    po_number = models.CharField(max_length=100)
    vendor = models.ForeignKey(vender_model,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField()

class historical_perfomance(models.Model):
    vendor = models.ForeignKey(vender_model,on_delete=models.CASCADE)
    date = models.DateField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
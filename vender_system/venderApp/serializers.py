from rest_framework import serializers
from .models import *

class dataserializer(serializers.ModelSerializer):
    class meta:
        model = vender_model,purchase_order,historical_perfomance
        fields = ('name','contact_details ','address','vender_code','on_time_delivery_rate','quality_rating_avg','fulfillment_rate'),
        ('po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgement_date'),
        ('vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')    
                
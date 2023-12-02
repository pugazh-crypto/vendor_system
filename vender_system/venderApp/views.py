from django.shortcuts import render
from venderApp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import dataserializer
# Create your views here.
@api_view(['GET'])
def vender_details(request):
    vender_data = vender_model.objects.all()
    serializer = dataserializer(vender_data, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def purchase_details(request):
    purchase_data = vender_model.objects.all()
    purchase_serializer = dataserializer(purchase_data,many=True)
    return Response(purchase_serializer.data)
@api_view(['GET'])
def historical_details(request):
    historical_data = vender_model.objects.all()
    history_serializer = dataserializer(historical_data,many = True)
    return Response(history_serializer.data)
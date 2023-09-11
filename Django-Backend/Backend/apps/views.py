from django.shortcuts import render
from django.http import HttpResponse
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EnergyData
from .serializers import EnergyDataSerializer

@api_view(['GET'])
def energy_data_list(request):
    if request.method == 'GET':
        energy_data = EnergyData.objects.all()
        serializer = EnergyDataSerializer(energy_data, many=True)
        return Response(serializer.data)



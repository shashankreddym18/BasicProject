
import math

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Frequency
from .serializers import FrequencySerializer
from django.shortcuts import render

def gui_view(request):
    return render(request, 'sinewave/gui.html')


class FrequencyView(APIView):
    def get(self, request):
        frequencies = Frequency.objects.all()
        serializer = FrequencySerializer(frequencies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FrequencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def generate_sine_wave(frequency):
    # Generate sine wave data using frequency
    # Code for generating the sine wave goes here
    return sine_wave_data

def transfer_sine_wave():
    frequencies = Frequency.objects.all()
    for frequency in frequencies:
        sine_wave_data = generate_sine_wave(frequency.value)
        # Transfer sine wave data over the internet using REST API
        response = requests.post('http://example.com/api/sinewave/', data=sine_wave_data)
        if response.status_code == 201:
            print('Sine wave data transferred successfully.')


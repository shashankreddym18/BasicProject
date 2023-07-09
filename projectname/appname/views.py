from django.shortcuts import render
from .models import SensorData

def monitoring_view(request):
    # Retrieve sensor data for the patient
    patient_id = 1  # Assuming patient ID 1 for demonstration
    sensor_data = SensorData.objects.filter(patient_id=patient_id).order_by('-timestamp')[:10]

    context = {
        'sensor_data': sensor_data,
    }
    return render(request, 'monitoring.html', context)

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    # Add more patient-related fields as needed

class SensorData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    heart_rate = models.IntegerField()
    blood_pressure = models.CharField(max_length=20)
    # Add more sensor data fields as needed

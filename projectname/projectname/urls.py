from django.urls import path
from .views import monitoring_view

urlpatterns = [
    path('monitoring/', monitoring_view, name='monitoring'),
]

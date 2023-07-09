from django.urls import path
from sinewave.views import FrequencyView
from sinewave.views import gui_view

urlpatterns = [
    path('api/frequencies/', FrequencyView.as_view(), name='frequency_api'),
    path('gui/', gui_view, name='gui'),
]



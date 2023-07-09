from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sine_wave(request):
    if request.method == 'POST':
        frequency = float(request.POST.get('frequency'))
        # Generate the sine wave using the provided frequency
        x = np.arange(0, 2 * np.pi, 0.1)
        y = np.sin(frequency * x)

        # Transfer the generated wave or perform other necessary actions with it
        # ...

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

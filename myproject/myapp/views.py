from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def start_animation(request):
    # Your backend logic to handle the animation request
    return JsonResponse({'status': 'Animation started!'})

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'state_of_watering/templates/state_of_watering/index.html')

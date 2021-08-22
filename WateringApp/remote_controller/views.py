from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .forms import ProgramatorForm
# Create your views here.

def index(request):
    form = ProgramatorForm(request.GET or None)
    if form.is_valid():
        form.save()
        form = ProgramatorForm()
    context = {
        'form' : form
    }
    return render(request, 'remote_controller/templates/remote_controller/index.html', context)
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Flow

from .forms import FlowForm

# Create your views here.
def index(request):
    flow_db_list = Flow.objects.order_by('-pub_date')
    context = {'flow_db_list' : flow_db_list}
    return render(request, 'flow_DB/templates/flow_DB/index.html', context)

def record_add_view(request):
    form = FlowForm(request.GET or None)
    if form.is_valid():
        form.save()
        form = FlowForm()
    context = {
        'form' : form
    }
    return render(request, 'flow_DB/templates/flow_DB/add.html', context)
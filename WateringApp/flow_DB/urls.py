from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.record_add_view, name='create')
]
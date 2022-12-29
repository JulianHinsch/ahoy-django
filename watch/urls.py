from django.urls import path
from . import views

urlpatterns = [
    path('', views.watch_schedule, name='watch_schedule'),
    path('<stream_id>', views.watch, name='watch'),
]
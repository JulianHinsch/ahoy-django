from django.urls import path
from . import views

urlpatterns = [
    path('', views.listen_schedule, name='listen_schedule'),
    path('<stream_id>', views.listen, name='listen'),
]
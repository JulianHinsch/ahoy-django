from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.schedule, name='schedule'),
    path('listen/', views.listen, name='listen'),
    path('watch/', views.watch, name='watch'),
]
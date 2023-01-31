from django.urls import path
from . import views

urlpatterns = [
    path('browse/', views.browse, name='browse'),
    path('watch/<film_id>', views.watch, name='watch'),
]
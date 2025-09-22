from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('day/<int:day>', views.days_week_whit_number, name='day-number'),  # /message/<day> (numérico)
    path('day/<str:day>', views.days_week, name='day-string'),  # /message/<day> (texto)
]

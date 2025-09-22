from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>', views.days_week_whit_number, name='day'),# /message/<day>
    path('<str:day>', views.days_week, name='day'),# /message/<day>
]

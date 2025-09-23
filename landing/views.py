from django.shortcuts import render
from datetime import date
#from .models import Alumno


# Create your views here.
def home(request):
    my_dic = {'nombre': 'Miguel','apellido': 'Aude','edad': 41}
    # alumnos_activos = Alumno.objects.filter(fecha_creacion__gte="05/07/2023")
    today = date.today()
    return render(request, 'landing/landing.html', {'name': 'Django','my_dic': my_dic,'today': today})

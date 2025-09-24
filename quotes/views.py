from django.shortcuts import render
from django.http import Http404


days_of_week = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo',
    'lunes': 'Lunes',
    'martes': 'Martes',
    'miércoles': 'Miércoles',
    'jueves': 'Jueves',
    'viernes': 'Viernes',
    'sábado': 'Sábado',
    'domingo': 'Domingo',
}

# Frases para cada día
frases = {
    'Lunes': '¡Comienza la semana con energía!',
    'Martes': 'Sigue avanzando, ya es martes.',
    'Miércoles': 'Mitad de semana, ¡ánimo!',
    'Jueves': 'Ya casi es viernes, no te rindas.',
    'Viernes': '¡Por fin viernes!',
    'Sábado': 'Disfruta tu sábado.',
    'Domingo': 'Relájate, es domingo.',
}

def index(request):
  try:
    dias = [1, 2, 3, 4, 5, 6, 7, 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    days = []
    for d in dias:
        days.append({
            'value': d,
            'type': 'int' if isinstance(d, int) else 'str',
            'name': days_of_week[d]
        })
    return render(request, 'quotes/index.html', {'days': days})
  except KeyError :
    render(request, '404.html', status=404)

# Vista para día por número
def days_week(request, day):
  try:
    nombre = days_of_week.get(day)
    frase = frases.get(nombre, '¡Buen día!')
    return render(request, 'quotes/day.html', {'nombre': nombre, 'frase': frase})
  except KeyError :
    render(request, '404.html', status=404)

# Vista para día por string
def days_week_whit_str(request, day):
  try:
    nombre = days_of_week.get(day)
    frase = frases.get(nombre, '¡Buen día!')
    return render(request, 'quotes/day.html', {'nombre': nombre, 'frase': frase})
  except KeyError :
    render(request, '404.html', status=404)
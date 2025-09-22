from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_of_week = {
    "Monday": "<p>Ser o no ser <strong>esa es la cuestion</strong></p>",
    "Tuesday": "<p>Pienso luego <strong>existo</strong></p>",
    "Wednesday": "<p>Vive como <strong>si fuera el ultimo dia</strong></p>",
    "Thursday": "<p>Da un poquito mas <strong>todos los dias</strong></p>",
    "Friday": "<p>Solo sé <strong>que no sé nada</strong></p>",
    "Saturday": "<p>Y en el fin del mundo, <strong>será mejor</strong></p>",
    "Sunday": "<p>Vive y <strong>deja vivir</strong></p>"
}

def index(request):
    list_items=""
    days = list(days_of_week.keys())
    for day in days:
        list_items += f"<li><a href=\"{reverse('day-number', args=[days.index(day) + 1])}\">{day}</a></li>"
    return HttpResponse(f"<ul>{list_items}</ul>")

def days_week_whit_number(request, day):
  days_list = list(days_of_week.keys())
  if 1 <= day <= len(days_list):
    day_name = days_list[day - 1]
    return HttpResponse(days_of_week[day_name])
  # Número fuera de rango: redirigimos a la ruta de string con 'Sunday'
  redirect_path = reverse('day-string', kwargs={'day': 'Sunday'})
  return HttpResponseRedirect(redirect_path)

def days_week(request, day):
  # Normalizamos el texto del día para que sea insensible a mayúsculas/minúsculas
  day_norm = str(day).strip().capitalize()
  quote_text = days_of_week.get(day_norm)
  if quote_text is None:
    return HttpResponseNotFound('Day not found')
  return HttpResponse(quote_text)

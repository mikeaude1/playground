from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

# Create your views here.

days_of_week = {
    "Monday": "Ser o no ser esa es la cuestion",
    "Tuesday": "Hola martes",
    "Wednesday": "Hola miercoles",
    "Thursday": "Hola jueves",
    "Friday": "Hola viernes",
    "Saturday": "Hola sabado",
    "Sunday": "Hola domingo"
}

def days_week_whit_number(request, day):
  quote_text = days_of_week.get(day, None)
  index = 0
  for key, value in days_of_week.items():
    if day == index:
      quote_text = value
      break
    index += 1
  else:
    return HttpResponseRedirect("/message/Sunday")
  return HttpResponse(quote_text)

def days_week(request, day):
  quote_text = days_of_week.get(day, None)
  if quote_text:
    return HttpResponse(quote_text)
  else:
    return HttpResponseNotFound("No Hay Frase Para Este Dia")
  return HttpResponse(quote_text)

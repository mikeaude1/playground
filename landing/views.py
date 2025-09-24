from django.shortcuts import render
from datetime import date
from django.http import HttpResponse, Http404

# Create your views here.
def home(request):
    try:
        stack = [
            {'id':'python','name':'Python'},
            {'id':'django','name':'Django'},
            {'id':'flask','name':'Flask'},
            {'id':'react','name':'React'},
            {'id':'vue','name':'Vue'},
            {'id':'angular','name':'Angular'},
            {'id':'node','name':'Node'},
            {'id':'express','name':'Express'},
            {'id':'mongodb','name':'MongoDB'}
        ]
        my_dic = {'nombre': 'Miguel','apellido': 'Aude','edad': 41}
        today = date.today()
        return render(request, 'landing/landing.html', {
            'name': 'Django',
            'my_dic': my_dic,
            'today': today,
            'stack': stack
        })
    except KeyError:
        raise Http404('Tecnologia no encontrada')

def stack_detail(request, tool):
    return HttpResponse(f'Tecnologia {tool}')

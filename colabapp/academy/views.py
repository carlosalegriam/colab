from django.shortcuts import render
from .models import Course

# Create your views here.
def v_index(request):
    context = {
        'coursel': Course.objects.get(name = 'Matematica Avanzada'),
        'course2': Course.objects.get(name = 'Lógica de programación'),
    }
    return render(request, 'index.html', context)

def v_course(request):
    context = {
        'course': Course.objects.get(id = course_id)
    }
    return render(request, 'course.html', context)


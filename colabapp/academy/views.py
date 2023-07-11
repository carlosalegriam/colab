from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {}
    return render(request, 'index.html', context)

def v_course(request):
    context = {}
    return render(request, 'course.html', context)


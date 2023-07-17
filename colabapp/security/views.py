from django.shortcuts import render
from security.forms import StudentForm
from django.contrib.auth.models import Permission

# Create your views here.
def v_signup(request):
    if request.method == 'POST':
        data = request.POST.copy() # tomo todos los datos del frontend
        data['username'] = data['email'] # Alteramos previamente

        form = StudentForm(data) # Comparo con el backend
        if form.is_valid(): # Valido
            us = form.save() # Se guarda en base de datos, creando el registro

            us.is_staff = True # Doy mas capacidades a ese registros de db
            us.is_active = True # Doy mas capacidades a ese registros de db
            us.set_password(data['password']) # Se Cifra la contrasena
            us.save() # Se vuelve a guardar en bd para actualizar en db
            perm = Permission.objects.get(name = "Can add subscription")
            us.user_permissions.add(perm) # Asignamos permiso

        else:
            print("sdfsdfsdfsdfsdf", form.errors)

    context = {}
    return render(request, 'signup.html', context)
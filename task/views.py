from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError # para integridad de la base de datso
from django.utils import timezone
from django.contrib.auth.decorators import login_required  # Decorarod para Proteger rutas
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return  render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', 
                      {"form": UserCreationForm}
                      )
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                #Guarda en la base y redirecciona
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                #VALIDO EN SERVER con una sesion en cookies
                login(request, user)
                return redirect('task')
           
                #Integrity Error para manejar errore de la base
            except IntegrityError:
                  return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."}) 
        
        
        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
 

@login_required  #Proteger Ruta
def task(request):
    #Listar Tareas 
    #tasks= Task.objects.all() # Retorna todas las tareas  
    #tasks= Task.objects.filter(user=request.user) # Retorna todas las tareas del user registrado
    tasks= Task.objects.filter(user=request.user,datecomleted__isnull=True ) # Retorna todas las tareas del user registrado a una fecha vacia 
    
    return  render(request, 'task.html', {'tasks': tasks})


@login_required  #Proteger Ruta
#Muestra Tareas completadas
def task_completed(request):
    tasks = Task.objects.filter(user=request.user, datecomleted__isnull=False).order_by('-datecomleted')
    return render(request, 'task.html', {"tasks": tasks})

@login_required  #Proteger Ruta
def task_detail(request, task_id):

    #Si vienen por GET Muestra 
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task) #Muestra el formulario en taskdetail para ver los datos 
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else: # Si quieres Actualizar los datos 
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user) # Debe conicidr con el usuario pasandor el user
            form = TaskForm(request.POST, instance=task) # toma las nuevas tareas del nuevo formulario y se guarda 
            form.save()
            return redirect('task')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})
 



@login_required
def signout(request):
    logout(request)
    return redirect('home')
    

def signin(request):
    #Autenticar el User de djngo
   
    if request.method == 'GET':
         return render (request, 'signin.html', {'form':AuthenticationForm})
    else:
         #Metodo para autenticar el ususario de la Base de Datos
         # Retorna un usurio valido o no  
         user= authenticate(request, username= request.POST['username'], password= request.POST['password'])
         
         if user is None: # Si no fue valido vuelvo al formulario
            return render (request, 'signin.html', {
                'form':AuthenticationForm, 
                'error':'Username or Password is incorrect'
                })
         else:
             #Si es valido guardo la sesion y lo mando a Task
             login(request,user)
             return redirect('task')
         
@login_required  #Proteger Ruta
# Les paso el formulario creado con los campos que le indique en forms
def create_task(request):

    #Cunado visto a la pagina
    if request.method == 'GET':
        return  render(request,'create_task.html', {'form':TaskForm })
    else: 
        try:
            # POST para poder guardar los datos en la base 
            form=TaskForm(request.POST) # paso los valores 
            #print (form)
            new_task=form.save(commit=False)
            new_task.user=request.user
            new_task.save()     
        except ValueError: 
            return render(request,'create_task.html', {
                'form':TaskForm, 
                'error':'Please provide valida data'
                  })  
            
    return  redirect('task')


@login_required  #Proteger Ruta
def complete_task(request, task_id):
    #Busco el usuario
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        #Grabo la hora de finalizados
        task.datecomleted = timezone.now()
        task.save()
        return redirect('task')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task')
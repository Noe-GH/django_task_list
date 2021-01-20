from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    # Si la plantilla usada regresa una petición con el método POST (Cuando se
    # oprime el botón Enviar):
    if request.method == 'POST':
        # Se utiliza el ModelForm recibiendo el método POST de la petición.
        # Esto crea un nuevo elemento.
        form = TaskForm(request.POST)
        # Se revisa si es válido. Si lo es, se guarda.
        if form.is_valid():
            form.save()
            # Se redirige a la misma URL.
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


# pk es por primary key, pero no necesariamente debe llamarse así.
def update_task(request, pk):
    # Consulta que obtiene el id.
    task_id = Task.objects.get(id=pk)
    # ModelForm. Aquí recibe instance con los datos para el id deseado para
    # que el formulario se llene con ellos.
    form = TaskForm(instance=task_id)
    context = {'form': form}

    if request.method == 'POST':
        # Usando POST y especificando la instancia es como se hacen
        # modificaciones.
        form = TaskForm(request.POST, instance=task_id)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        # Para borrar de la base de datos:
        item.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', context)

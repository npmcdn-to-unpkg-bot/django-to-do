from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import task
# Create your views here.


def index(request):
    latest_task = task.objects.all()
    context = {'latest_task': latest_task}
    return render(request, 'tasks/index.html', context)

def new(request):
    return render(request, 'tasks/new.html')

def create(request):
    if request.method == 'POST':
        create_task = task(
            name=request.POST['name'],
            description=request.POST['description'],
            created=timezone.now()
        )
        create_task.save()
    return HttpResponseRedirect(reverse('tasks:index'))

def show(request, task_id):
    show_task = get_object_or_404(task, pk=task_id)
    return render(request, 'tasks/show.html', {'task': show_task})


def edit(request, task_id):
    edit_task = get_object_or_404(task, pk=task_id)
    try:
        selected_name = task.objects.get(pk=request.POST['name'])
    except (KeyError, task.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'tasks/edit.html', {
            'task': task,
            'error_message': "You didn't select a Task",
        })
    else:
        edit_task.name = selected_name
        edit_task.save()
        return HttpResponseRedirect(reverse('tasks:show', args=(task.id,)))


def delete(request, task_id):
    delete_task = get_object_or_404(task, pk=task_id)
    delete_task.delete()
    return HttpResponseRedirect(reverse('tasks:index'))
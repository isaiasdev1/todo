from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CategoriaForm, TarefaForm
from .models import Categoria, Tarefa

# Create your views here.


@login_required
def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:lista_categorias')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/nova_categoria.html', {'form': form})


@login_required
def lista_categorias(request):
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'tarefas/lista_categorias.html', {'categorias': categorias})


@login_required
def editar_categoria(request, id_categoria):
    categoria = get_object_or_404(
        Categoria, id=id_categoria, user=request.user)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'tarefas/nova_categoria.html', {'form': form})


@login_required
def delete_categoria(request, id_categoria):
    Categoria.objects.get(id=id_categoria).delete()
    return redirect('tarefas:lista_categorias')


@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core')
        else:
            print(form.errors)
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})


@login_required
def delete_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa).delete()
    return redirect('core')


@login_required
def editar_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('core')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def home(request):
    return render(request, 'home.html')



# --- FUNÇÕES DE CRUD PARA UM ITEM ---

# READ (Listar)
def list_items(request):
    itemss = Item.objects.all()
    return render(request, 'items_list.html', {'items': itemss})

# CREATE (Criar)
def create_items(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_items')
    return render(request, 'items_form.html', {'form': form})

# UPDATE (Editar)
def edit_items(request, id):
    items = get_object_or_404(items, id=id)
    form = ItemForm(request.POST or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('list_items')
    return render(request, 'items_form.html', {'form': form})

# DELETE (Deletar)
def delete_items(request, id):
    items = get_object_or_404(items, id=id)
    if request.method == 'POST':
        items.delete()
        return redirect('list_items')
    return render(request, 'items_confirm_delete.html', {'items': items})
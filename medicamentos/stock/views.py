from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Medicamento, Proveedor, Cliente, Pedido,User
from .forms import MedicamentoForm, ClienteForm, ProveedorForm, PedidoForm, RegistrationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio.html')
def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('inicio.html')
@login_required
def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'lista_medicamentos.html', {'medicamentos': medicamentos})
@login_required
def detalle_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)
    return render(request, 'detalle_medicamento.html', {'medicamento': medicamento})
@permission_required('stock.add_medicamento')
def alta_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'alta_medicamento.html', {'form': form})

@permission_required('stock.change_medicamento')
def editar_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('detalle_medicamento', medicamento_id=medicamento.id)
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'editar_medicamento.html', {'medicamento': medicamento, 'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')


@login_required
def cargar_pedido(request):
    form = PedidoForm(request.POST)
    if form.is_valid():
        pedido = form.save()
        return redirect('lista_pedidos')
    return render(request, 'pedido.html', {'form': form})

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    context = {'pedidos': pedidos}
    return render(request, 'lista_pedidos.html', context)

@login_required
def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, id=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('lista_medicamentos')
    return render(request, 'eliminar_medicamento.html', {'medicamento': medicamento})

@login_required
def alta_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alta_cliente')
    else:
        form = ClienteForm()
    context = {'form': form}
    return render(request, 'alta_cliente.html', context)

@login_required
def alta_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    context = {'form': form}
    return render(request, 'alta_proveedor.html', context)

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'lista_clientes.html', context)

@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor_id')
        proveedor = Proveedor.objects.get(pk=proveedor_id)
        proveedor.delete()
        return redirect('lista_proveedores')

    context = {
        'proveedores': proveedores
    }
    return render(request, 'lista_proveedores.html', context)

@login_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '¡Registro exitoso! Por favor inicia sesión.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'registration_form': form})
@login_required
def profile_view(request):
    return render(request, 'profile.html')
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form})
def eliminar_proveedor(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor_id')
        proveedor = Proveedor.objects.get(pk=proveedor_id)
        proveedor.delete()
    return redirect('lista_proveedores')
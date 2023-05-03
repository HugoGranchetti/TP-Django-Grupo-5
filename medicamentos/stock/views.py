from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Medicamento, Proveedor,Cliente
from .forms import MedicamentoForm,ClienteForm, ProveedorForm,Pedido,PedidoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm

def inicio(request):
    return render(request,'inicio.html')

def index(request):
    return render(request, 'index.html')

def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'lista_medicamentos.html', {'medicamentos': medicamentos})

def detalle_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, pk=medicamento_id)
    return render(request, 'detalle_medicamento.html', {'medicamento': medicamento})

def alta_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'alta_medicamento.html', {'form': form})

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

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            message = "Correo electrónico o contraseña incorrectos."
    else:
        message = ""

    return render(request, 'login.html', {'message': message})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def cargar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            
            pedido = form.save(commit=False)
            pedido.productos_id = request.POST['productos_id']
            pedido.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedido.html', {'form': form})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    context = {'pedidos': pedidos}
    return render(request, 'lista_pedidos.html', context)

def eliminar_medicamento(request, pk):
    medicamento = Medicamento.objects.get(id=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('lista_medicamentos')
    context = {'medicamento': medicamento}
    return render(request, 'eliminar_medicamento.html', context)

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

def alta_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alta_proveedor.html')
    else:
        form = ProveedorForm()
    context = {'form': form}
    return render(request, 'alta_proveedor.html', context)

def lista_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'lista_clientes.html', context)

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {'proveedores': proveedores}
    return render(request, 'lista_proveedores.html', context)

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    else:
        return render(request, 'eliminar_cliente.html', {'cliente': cliente})
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Aquí puede agregar cualquier lógica adicional, como enviar un correo electrónico de bienvenida, etc.
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'registration_form': form})
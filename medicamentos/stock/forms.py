from django import forms
from .models import Medicamento
from .models import Pedido
from django.forms.widgets import SelectDateWidget
import datetime
from .models import Cliente, Proveedor
from .models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cuit': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'cantidad', 'fecha_vencimiento', 'proveedor', 'precio', 'lote']

from django import forms
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
import datetime

from .models import Pedido, Medicamento, Cliente, Proveedor


from django import forms
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
import datetime

from .models import Pedido, Medicamento, Cliente, Proveedor


class PedidoForm(forms.ModelForm):
    productos = forms.ModelChoiceField(
        queryset=Medicamento.objects.all(),
        widget=forms.RadioSelect
    )
    nombre_cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.RadioSelect
    )
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        widget=forms.RadioSelect
    )
    fecha_pedido = forms.DateField(
        widget=SelectDateWidget(),
        initial=datetime.date.today
    )

    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'fecha_pedido', 'cantidad', 'productos', 'proveedor', 'archivo']

    def clean_fecha_pedido(self):
        fecha_pedido = self.cleaned_data['fecha_pedido']
        if fecha_pedido < timezone.now().date():
            raise forms.ValidationError("La fecha del pedido no puede ser anterior a la fecha actual.")
        return fecha_pedido

    def save(self, commit=True):
        pedido = super().save(commit=False)
        if commit:
            pedido.save()
        pedido.productos.add(self.cleaned_data['productos'].id)
        return pedido


    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email', 'password']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
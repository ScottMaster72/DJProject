from django import forms
from .models import Articulo
from .models import Registro
from .models import Proovedores
from .models import Pedido



class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'

class ProovedoresForm(forms.ModelForm):
    class Meta:
        model = Proovedores
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
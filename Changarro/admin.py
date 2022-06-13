from django.contrib import admin
from .models import Articulo
from .models import Registro
from .models import Proovedores
from .models import Sucursales
from .models import Consola
from .models import Promociones
from .models import Merma
from .models import Pedido
# Register your models here.
admin.site.register(Articulo)
admin.site.register(Registro)
admin.site.register(Proovedores)
admin.site.register(Sucursales)
admin.site.register(Consola)
admin.site.register(Promociones)
admin.site.register(Merma)
admin.site.register(Pedido)
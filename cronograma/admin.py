from django.contrib import admin
from .models import Cronograma, Capilla, Musico, Misa

admin.site.register(Capilla)
admin.site.register(Musico)
admin.site.register(Cronograma)
admin.site.register(Misa)

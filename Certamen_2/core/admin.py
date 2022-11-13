
from django.contrib import admin

# Register your models here.
from .models import Residencia
from .models import Correspondencia

admin.site.register(Residencia)
admin.site.register(Correspondencia)

from django.shortcuts import render

from .models import Correspondencia , Residencia

def home(request):
    resultado=(request.GET.get("buscador"))
    corres = Correspondencia.objects.all()
    return render(request,'core/index.html', {"corres": corres})

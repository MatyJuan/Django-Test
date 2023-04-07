from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import QR


@login_required
def home(request):
    context = {
        "qrs": QR.objects.all()
    }
    return render(request, "index.html", context=context)

def cerrar_sesion(request):
    logout(request)
    return redirect('/')


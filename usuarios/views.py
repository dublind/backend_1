from django.shortcuts import render


def perfil(request):
    equipo = [
        {"nombre": "Ignacio Salinas", "rol": "Desarrollo backend"},
        {"nombre": "Diego Pérez", "rol": "Interfaz y documentación"},
    ]
    return render(request, "usuarios/perfil.html", {"equipo": equipo})

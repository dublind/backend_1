from django.http import Http404
from django.shortcuts import render

from .data import PRODUCTOS


def inicio(request):
    destacados = [producto for producto in PRODUCTOS.values() if producto["destacado"]]
    return render(request, "productos/index.html", {"destacados": destacados})


def catalogo(request):
    categoria = request.GET.get("categoria", "todas")
    productos = list(PRODUCTOS.values())
    if categoria != "todas":
        productos = [p for p in productos if p["categoria"].lower() == categoria.lower()]
    return render(
        request,
        "productos/catalogo.html",
        {"productos": productos, "categoria_actual": categoria},
    )


def detalle(request, producto_id):
    producto = PRODUCTOS.get(producto_id)
    if producto is None:
        raise Http404("Producto no encontrado")
    return render(request, "productos/detalle.html", {"producto": producto})

from django.test import TestCase
from django.urls import reverse


class TiendaViewsTests(TestCase):
    def test_inicio_responde_y_muestra_destacados(self):
        response = self.client.get(reverse("productos:inicio"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Audífonos Pulse Pro")

    def test_catalogo_muestra_cuatro_productos(self):
        response = self.client.get(reverse("productos:catalogo"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["productos"]), 4)

    def test_filtro_de_categoria(self):
        response = self.client.get(reverse("productos:catalogo"), {"categoria": "audio"})
        self.assertEqual(len(response.context["productos"]), 2)

    def test_detalle_valido(self):
        response = self.client.get(reverse("productos:detalle", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "59990")

    def test_detalle_inexistente_devuelve_404(self):
        response = self.client.get(reverse("productos:detalle", args=[99]))
        self.assertEqual(response.status_code, 404)

    def test_pagina_equipo(self):
        response = self.client.get(reverse("usuarios:perfil"))
        self.assertContains(response, "Ignacio Salinas")
        self.assertContains(response, "Diego Pérez")

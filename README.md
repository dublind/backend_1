# Nexo Store

Proyecto de evaluación de Programación Backend desarrollado por Ignacio Salinas y Diego Pérez. Es una tienda online construida con Django y Bootstrap.

## Requisitos cumplidos

- Proyecto Django separado en las apps `productos` y `usuarios`.
- Menú con las rutas Inicio, Catálogo y Nosotros.
- Catálogo de cuatro productos y vista de detalle.
- Datos almacenados en un diccionario de Python.
- Uso de plantillas, archivos estáticos, imágenes e identidad visual.
- Diseño adaptable con Bootstrap 5.

## Instalación

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/`.

## Pruebas

```powershell
python manage.py test
```

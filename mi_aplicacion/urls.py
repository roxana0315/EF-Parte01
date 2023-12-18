from django.urls import path
from .views import Paises, RegistrarPais, Editoriales, CrearEditorial, index

urlpatterns = [
    path('Paises/', Paises, name='Paises'),
    path('RegistrarPais/',RegistrarPais, name='RegistrarPais'),
    path('Editoriales/', Editoriales, name='Editoriales'),
    path('CrearEditorial/',CrearEditorial, name='CrearEditorial'),
    path('', index, name='index'),  # Importa la función index
    # ... otras rutas de la aplicación ...
]

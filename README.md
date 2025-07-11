# Aplicación CRUD y django

### ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web? Añade un ejemplo de aplicación web que use una estructura de CRUD
CRUD (Create, Read, Update, Delete) es un concepto fundamental en el desarrollo de software para la gestión de datos 
dentro de las aplicaciones. Se refiere a las cuatro operaciones básicas que se realizan sobre los datos: crear, leer, 
actualizar y eliminar. Estas operaciones permiten a los desarrolladores interactuar con datos persistentes almacenados 
en bases de datos u otros sistemas de almacenamiento de datos.

Las aplicaciones web suelen implementar estas operaciones para gestionar datos de usuarios, productos, o cualquier otro
tipo de información relevante. Por ejemplo, una tienda en línea utiliza operaciones CRUD para manejar catálogos de 
productos, inventario y datos de clientes.  REST, que se usa en el diseño de aplicaciones WEB, emplea operaciones HTTP 
que corresponden directamente con las funciones CRUD (GET, PUT, PUSH, and DELETE).

### ¿Qué son los patrones de arquitectura en desarrollo de software?
- _¿Qué es el patrón MVC (Modelo–Vista–Controlador)?_
 
 El patrón MVC separa la lógica de una aplicación en tres componentes distintos: el modelo, la vista y el controlador.
 El modelo se encarga de gestionar los datos y la lógica de negocio, la vista es responsable de la representación de la
 información al usuario, y el controlador actúa como intermediario entre el modelo y la vista, manejando las entradas 
 del usuario y actualizando el modelo o la vista según sea necesario

- _¿Qué es el patrón MVT (Modelo–Vista–Template)?_

Este patrón es una variante del patrón MVC (Modelo-Vista-Controlador) utilizado ampliamente en el diseño de software. 
El patrón MVT divide la estructura de una aplicación en tres partes interconectadas, lo que permite un desarrollo más 
ordenado y menos complicado. Las tres partes son: el Modelo, la Vista y la Plantilla. El Modelo se refiere a la 
estructura de datos, la vista es el lugar donde se establece la lógica de negocio y la plantilla es donde se muestra el
resultado.

- _Diferencias entre MVC y MVT._

La principal diferencia es que en el patrón MVC, debemos escribir toda la lógica de control, mientras que en el patrón
MVT, la lógica de control ya esta implementada.

- ¿Cuál de estos dos patrones se usa en Django?

Django usa el patrón MVT.

### ¿Cómo se estructura un proyecto en Django? Explicar brevemente el rol de los modelos, vistas, templates y URLs.
Para crear un proyecto en django, primero debemos ejecutar lo siguiente:
```commandline
django-admin startproject <mysite> .
```
Esto creará lo siguiente:
- El fichero _manage.py_, que nos ayuda con la administración del proyecto.
- Una carpeta de nombre _\<mysite\>_ que contiene la configuración básica del proyecto. Entre otros, estan los 
siguientes archivos:
  - El archivo _settings.py_ contiene la configuración web de tu proyecto.
  - El archivo _urls.py_ contiene una lista de los patrones utilizados para resolver las distintas páginas web de tu
proyecto.

Esto nos da la estructura básica de un proyecto en django, pero también necesitamos una aplicación. Para ello, 
ejecutamos el siguiente comando:
```commandline
python manage.py startapp <myapp>
```
Esto creará una carpeta con el nombre _\<myapp\>_ con el siguiente contenido:
```commandline
└── <myapp>
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
    └── wsgi.py
```
Con esto ya podríamos empezar a trabajar en nuestro proyecto django.

### ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?

### ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD, para qué es cada una? (Por ejemplo: startapp, makemigrations, migrate, runserver, ModelForm, admin, etc.)

### ¿Cómo funciona el Admin de Django?
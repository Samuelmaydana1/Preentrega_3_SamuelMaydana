My Django Book Application
Descripción
Esta aplicación web, desarrollada con Django, permite gestionar libros y sus categorías. El proyecto implementa el patrón MVT (Model-View-Template) y está diseñado para ser un sistema básico para agregar, buscar y listar libros y categorías.

Funcionalidades
Añadir Autor: Permite agregar nuevos autores a la base de datos.
Añadir Categoría: Permite agregar nuevas categorías para clasificar libros.
Añadir Libro: Permite agregar libros, asociándolos con un autor y una categoría.
Buscar Libros: Permite buscar libros en la base de datos por título.
Listar Categorías: Muestra todas las categorías disponibles en la base de datos.
Requisitos
Python 3.x
Django 4.x o superior
Instalación
Clona el Repositorio

bash
Copiar código
git clone [URL DEL REPOSITORIO]
cd [NOMBRE DEL REPOSITORIO]
Crea un Entorno Virtual

bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows, usa `env\Scripts\activate`
Instala las Dependencias

bash
Copiar código
pip install -r requirements.txt
Configura la Base de Datos

Si estás utilizando la base de datos SQLite (por defecto), no es necesario realizar configuraciones adicionales. Si usas otra base de datos, actualiza la configuración en myproject/settings.py.

Realiza las Migraciones

bash
Copiar código
python manage.py migrate
Crea un Superusuario (Opcional)

Para acceder al panel de administración de Django, crea un superusuario con el siguiente comando:

bash
Copiar código
python manage.py createsuperuser
Sigue las instrucciones para ingresar el nombre de usuario, correo electrónico y contraseña.

Ejecuta el Servidor de Desarrollo

bash
Copiar código
python manage.py runserver
Abre tu navegador y visita http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

Uso
Funcionalidades Principales
Añadir Autor

Navega a http://127.0.0.1:8000/add_author/
Completa el formulario para agregar un nuevo autor.
Añadir Categoría

Navega a http://127.0.0.1:8000/add_category/
Completa el formulario para agregar una nueva categoría.
Añadir Libro

Navega a http://127.0.0.1:8000/add_book/
Completa el formulario para agregar un nuevo libro, seleccionando un autor y una categoría previamente agregados.
Buscar Libros

Navega a http://127.0.0.1:8000/search_books/
Usa el formulario para buscar libros por título.
Listar Categorías

Navega a http://127.0.0.1:8000/list_categories/
Visualiza todas las categorías disponibles.
Estructura del Proyecto
myproject/: Directorio del proyecto principal.

settings.py: Configuración del proyecto Django.
urls.py: Rutas del proyecto.
wsgi.py: Punto de entrada WSGI para servidores de aplicaciones.
myapp/: Aplicación dentro del proyecto.

models.py: Definición de los modelos (Autor, Categoría, Libro).
views.py: Definición de las vistas (funcionalidades).
forms.py: Formularios para la entrada de datos.
templates/: Plantillas HTML.
urls.py: Rutas específicas de la aplicación.
Contribución
Si deseas contribuir al proyecto, por favor sigue estos pasos:

Haz un Fork del Repositorio
Crea una Nueva Rama
Haz tus Cambios
Haz un Pull Request
Asegúrate de seguir el estilo de código y de agregar pruebas para cualquier nueva funcionalidad.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Puedes usar, modificar y distribuir este software bajo los términos de esta licencia.

Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Nombre: [Tu Nombre]
Email: [Tu Email]
GitHub: [Tu Perfil de GitHub]

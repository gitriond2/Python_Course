# Blog Application

## Descripción
Desarrollo de una aplicación web para la gestión de un blog personal. Esta aplicación permite crear, editar y visualizar entradas de blog, así como gestionar los comentarios de los usuarios.

## Tecnologías Utilizadas
- Django
- HTML
- CSS

## Funcionalidades Principales
- Creación y edición de entradas de blog.
- Visualización de las entradas en el blog.
- Gestión de comentarios de los usuarios.

## Instalación
1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd blog_app
    ```
3. Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
1. Aplica las migraciones:
    ```bash
    python manage.py migrate
    ```
2. Ejecuta el servidor:
    ```bash
    python manage.py runserver
    ```
3. Accede a la aplicación en tu navegador en `http://localhost:8000`.

## Estructura del Proyecto
- **models.py**: Define los modelos de entrada de blog y comentarios.
- **views.py**: Contiene la lógica para la creación, edición y visualización de entradas de blog.
- **templates/blog**: Directorio con las plantillas HTML para las páginas del blog.

## Código Principal
```python
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Publish'))

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

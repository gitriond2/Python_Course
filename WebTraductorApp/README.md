# Translator Application

## Descripción
Desarrollo de una aplicación web de traducción utilizando Django y la API de Google Translate. Esta aplicación permite a los usuarios ingresar texto en un área de texto y recibir la traducción del texto ingresado en otro idioma.

## Tecnologías Utilizadas
- Django
- Google Translate API

## Funcionalidades Principales
- Formulario para ingreso de texto.
- Integración con la API de Google Translate para obtener la traducción.
- Renderizado de la página con el texto original y traducido.

## Instalación
1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd translator_app
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
- **views.py**: Contiene la lógica del traductor.
- **translate.py**: Archivo auxiliar para manejar la traducción utilizando la API de Google.
- **templates/translator.html**: Plantilla HTML para la interfaz del usuario.

## Código Principal
```python
from django.shortcuts import render
from . import translate

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = translate.translate(original_text)
        return render(request, 'translator.html', {'output_text': output, 'original_text': original_text})
    else:
        return render(request, 'translator.html')

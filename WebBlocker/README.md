# Website Blocker Script

Este script de Python se utiliza para bloquear y desbloquear sitios web específicos durante determinadas horas del día. Utiliza el archivo `hosts` de Windows para redirigir los sitios web a `127.0.0.1`, lo que efectivamente bloquea el acceso a dichos sitios.

## Requisitos

- Python 3.x
- Sistema operativo Windows

## Instrucciones

1. **Ubicación del archivo `hosts`**:
   - En un sistema Windows, el archivo `hosts` se encuentra en la siguiente ruta:
     ```
     C:\Windows\System32\drivers\etc\hosts
     ```

2. **Lista de sitios web a bloquear**:
   - Modifica la lista `website_list` en el script con los sitios web que deseas bloquear. Por defecto, se incluyen:
     ```python
     website_list = ["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]
     ```

3. **Horas de bloqueo**:
   - El script está configurado para bloquear los sitios web entre las 8 AM y las 6 PM. Puedes ajustar estas horas en la siguiente línea del código:
     ```python
     if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
     ```

## Uso

1. **Ejecución del script**:
   - Ejecuta el script de Python. Durante las horas de trabajo especificadas, los sitios web en `website_list` se bloquearán.
   - Fuera de las horas de trabajo, los sitios web se desbloquearán.

2. **Bloqueo de sitios web**:
   - Durante las horas de trabajo, el script añade las entradas correspondientes al archivo `hosts` para redirigir los sitios web a `127.0.0.1`.

3. **Desbloqueo de sitios web**:
   - Fuera de las horas de trabajo, el script elimina las entradas correspondientes del archivo `hosts`.

## Código

```python
import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Working hours...")
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

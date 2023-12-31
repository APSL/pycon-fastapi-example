# Guía paso a paso

## 6. Versionado y obsolescencia de endpoints

* Editar modelo para las pruebas.
* Generar un nuevo endpoint.
* Instalación de fastapi-versioning.
* Agregar versionado en main.py
* Generar la versión superior del endpoint anterior y marcar como deprecado el anterior.


## 5. Añadir logs a nuestra API

* Definir ruta del fichero de configuración de los logs en el settings.
* Añadir carga de la configuración de logs en main.py.
* Usar los logs importando `logging` y registrar de la mejor manera posible toda invocación a nuestros endpoints.


## 4. Agrupar el código y leer constantes de settings

* Instalación de pydantic-settings para las constantes del proyecto
* Mover a models/ los modelos
* Mover a routers/ los endpoints y agruparlos por tipo
* Generar settings para las constantes del proyecto
* Crear .env y .secrets para las constantes públicas y privadas
* Adaptar código en main.py
* Nuevo comando para ejecutar el proyecto: `python src/run.py`


## 3. Añadir validadores de esquemas y ORM

* Instalación de beanie (ODM [object-document mapper] basado en pydantic).
* Crear modelos para la validación de request y response de los endpoints.
* Actualizar endpoints con los modelos.
* Eliminar get_db, no será necesario gracias a beanie. 


## 2. Añadir endpoint con accesos a base de datos

* Instalación de "motor" (driver para conexiones a mongo de manera asíncrona).
* Creación de los endpoints GET /posts y POST /posts
* Creación de una instancia del driver, mongo_db.
* Creación una función para inyectar el driver a base de datos en cada endpoint.
* Añadir dos eventos a la API, que mantendrá el cliente de mongo abierto y tras morir el servidor matará el cliente.
* Probar en http://localhost:8000/docs


## 1. Creación servidor mínimo

Realizar la instalación de dependencias

```bash
pip install -r requirements.txt
```

Ejecutar servidor

```bash
uvicorn src.main:app --reload
```

Probar endpoints

* http://localhost:8000/ping
* http://localhost:8000/docs
* http://localhost:8000/static/image-unavailable.png

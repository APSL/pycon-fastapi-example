# Guía paso a paso

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

# Guía paso a paso


## Creación servidor mínimo

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

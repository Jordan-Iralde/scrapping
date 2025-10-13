# Scrapping de datos
La idea es extraer datos de productos, busquedas, headers de elementos, guardarlos y enviarlos hacia una tabla o varias para usarlas en power apps, power automate y power bi.
Si no es posible realizar web scrapping, debido a un robots.txt

## Primeros pasos
Instalar dependencias necesarias  de requirements.txt

## Mercado Libre
```
project/
│
├── README.md
├── requirements.txt
├── config.yaml
├── .env
│
├── main.py
│
├── core/
│   ├── __init__.py
│   ├── scraper.py          # Lógica principal de scraping
│   ├── parser.py           # Limpieza y extracción del HTML
│   ├── sheets_uploader.py  # Conexión y subida a Google Sheets
│   ├── utils.py            # Funciones auxiliares (reintentos, logs, etc.)
│   └── logger.py           # Configuración de logging

```

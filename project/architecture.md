```
project/
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
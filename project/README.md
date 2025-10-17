# Proyecto Scraper Híbrido

## Descripción
Scraper modular capaz de extraer datos de múltiples sitios, tanto estáticos como dinámicos (JS), y exportar en CSV separados por sitio.

## Estructura del proyecto
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

## Dependencias
- Python 3.13+
- requests
- beautifulsoup4
- pandas
- playwright

## Uso
1. Instalar dependencias:
pip install -r requirements.txt
playwright install
2. Configurar `config.yaml` con URLs y parámetros
3. Ejecutar:
python main.py
4. CSVs generados en `data/processed/`

## Extensiones futuras
- Conectar con Power BI / Power Apps
- Automatizar ejecución con Power Automate o scheduler
- Crear API REST para consumo web
README_idea.md (documento de concepto)

# Idea de Proyecto de Web Scraping

## Objetivo
Extraer datos de e-commerce (productos, precios, stock) y generar dashboards o apps para monitoreo y análisis.

## Beneficio
- Visualización de datos en Power BI / Power Apps
- Actualización automática mediante Power Automate
- Posibilidad de crear web apps para clientes o internos

## Tecnologías
- Python (requests, BeautifulSoup, Playwright)
- NodeJS + Express + Angular (opcional web)
- Power Platform (Power BI, Power Apps, Power Automate)

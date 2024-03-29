
# Herramientas de Conversión y Carga para OpenSearch

Este repositorio contiene dos scripts Python diseñados para facilitar la conversión de archivos Excel a JSON y posteriormente cargar esos archivos JSON en OpenSearch usando la API Bulk.

## xls_json_converter.py

Este script convierte archivos Excel (.xlsx) en archivos JSON. Los archivos JSON generados están formateados para ser compatibles con la API Bulk de Elasticsearch/OpenSearch.

### Uso

Para utilizar el script, ejecútalo y sigue las instrucciones en la interfaz gráfica para seleccionar un archivo Excel y guardarlo como JSON.

```bash
python xls_json_converter.py
```

## bulk_json_opensearch.py

Una vez que tienes un archivo JSON en el formato correcto, puedes usar este script para cargarlo en OpenSearch utilizando la API Bulk.

### Configuración

Antes de ejecutar el script, asegúrate de tener las credenciales y la URL de tu instancia de OpenSearch listas para usar.

### Uso

Ejecuta el script, ingresa los detalles solicitados en la interfaz gráfica, selecciona el archivo JSON a cargar y el script se encargará del resto.

```bash
python bulk_json_opensearch.py
```

## Requisitos

- Python 3
- Pandas
- Tkinter (debería estar incluido con Python)

## Instalación de Dependencias

Para instalar Pandas, puedes usar pip:

```bash
pip install pandas
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una sugerencia, por favor, abre un issue o un pull request.

---
title: Archivo de Excel y Operaciones con Datos
linktitle: Archivo y Operaciones con Datos
type: docs
weight: 10
url: /es/nodejs-cpp/mcp/file-operations
keywords: "Operaciones con archivos de Excel, operaciones con datos de Excel, crear libro de Excel, hoja de cálculo de Excel, leer datos de Excel, escribir datos de Excel"
description: "Operaciones con archivos y datos de Excel  crear libros de trabajo, gestionar hojas de cálculo, leer y escribir datos de Excel con automatización de IA"
---

# Archivo de Excel y Operaciones con Datos

Gestiona **archivos de Excel** y **operaciones con datos** con automatización impulsada por IA. Crea **libros de Excel**, gestiona **hojas de cálculo**, y realiza operaciones de lectura/escritura de **datos de Excel**.

## Herramientas Disponibles

- `create_workbook` - Crear nuevos **libros de Excel** con automatización de **IA para Excel**
- `create_worksheet` - Agregar **hojas de cálculo de Excel** a **libros de Excel** existentes
- `get_workbook_info` - Obtener metadatos e información del **libro de Excel**
- `read_data_from_excel` - Leer datos de **hojas de cálculo de Excel** con **precisión impulsada por IA**
- `write_data_to_excel` - Escribir datos en **hojas de cálculo de Excel** a través de **Excel MCP**

## Crear Libros de Excel

### Crear Libro Básico
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### Crear Libro con Hoja Personalizada
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## Gestionar Hojas de Cálculo

### Añadir Nueva Hoja de Cálculo
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### Obtener Información del Libro de Excel
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Escribir Datos en Excel

### Escribir Encabezados y Datos
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### Escribir datos en una posición personalizada
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## Leer datos de Excel

### Leer rango utilizado completo
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### Leer rango específico
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### Leer desde la posición predeterminada
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## Ejemplo completo de flujo de trabajo

### 1. Crear tu primer informe de Excel
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. Agregar hoja de resumen
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. Escribir datos de ventas
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. Verificar datos
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. Verificar la estructura del libro de trabajo
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## Mejores prácticas

1. **Rutas de archivos**: Usa rutas relativas para mejor portabilidad
2. **Nombres de hojas**: Usa nombres descriptivos para las hojas de trabajo
3. **Estructura de datos**: Organiza los datos con encabezados claros
4. **Lectura de rango**: Especifica rangos para conjuntos de datos grandes
5. **Manejo de errores**: Verifica la existencia del archivo antes de operaciones

## Patrones comunes

### Patrón de importación de datos
1. Crear libro de trabajo
2. Escribir datos sin procesar
3. Leer para verificar
4. Procesar con fórmulas

### Informes de Multiple Hoja
1. Crear libro de trabajo con hoja principal
2. Añadir hojas de resumen/análisis
3. Escribir datos en cada hoja
4. Enlazar hojas con fórmulas

### Validación de Datos
1. Escribir datos
2. Leer rangos específicos
3. Verificar integridad de datos
4. Manejar valores faltantes 
{{< app/cells/assistant language="nodejs-cpp" >}}

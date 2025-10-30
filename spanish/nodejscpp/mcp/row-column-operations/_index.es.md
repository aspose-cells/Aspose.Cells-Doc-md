---
title: Operaciones de filas y columnas en Excel
linktitle: Operaciones de filas y columnas
type: docs
weight: 50
url: /es/nodejs-cpp/mcp/row-column-operations
keywords: "Operaciones de filas, columnas, gestión del diseño en Excel, insertar filas, eliminar columnas, redimensionar celdas en Excel"
description: "Operaciones de filas y columnas en Excel  insertar, eliminar, redimensionar, ocultar/desocultar filas y columnas con automatización por IA"
---

# Operaciones de filas y columnas en Excel

Gestiona **operaciones de filas y columnas en Excel** con automatización habilitada por IA. Inserta, elimina, redimensiona, oculta/desoculta **filas** y **columnas** en Excel para una gestión perfecta del diseño de la hoja de cálculo.

## Herramientas disponibles

- `row_column_operations` - **Operaciones de filas/columnas en Excel** (insertar, eliminar, redimensionar, ocultar/desocultar) con **Excel IA**
- `row_column_operations_batch` - Realiza varias **operaciones de filas/columnas en Excel** en lote usando **Excel MCP**

## Operaciones individuales

### Insertar filas
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/layout-test.xlsx",
    "sheet_name": "Data",
    "operation": "insert_rows",
    "rows": "5",
    "count": 2
  }
}
```

### Eliminar columnas
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Sheet1",
    "operation": "delete_columns",
    "columns": "C:D"
  }
}
```

### Establecer altura de fila
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_row_height",
    "rows": "1",
    "height": 30
  }
}
```

### Establecer ancho de columna
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_column_width",
    "columns": "A:F",
    "width": 15
  }
}
```

## Operaciones por lote

### Configuración integral de diseño
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/professional-layout.xlsx",
    "sheet_name": "Summary Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "3",
        "height": 30
      },
      {
        "operation": "set_row_height",
        "rows": "4:6",
        "height": 20
      },
      {
        "operation": "set_column_width",
        "columns": "C",
        "width": 20
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      },
      {
        "operation": "auto_fit_rows",
        "rows": "7:10"
      }
    ]
  }
}
```

### Operaciones de inserción y eliminación
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/restructure.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "5",
        "count": 2
      },
      {
        "operation": "insert_columns",
        "columns": "D",
        "count": 1
      },
      {
        "operation": "delete_rows",
        "rows": "8:9"
      }
    ]
  }
}
```

### Operaciones de ocultar y mostrar
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/visibility.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "hide_rows",
        "rows": "15:16"
      },
      {
        "operation": "hide_columns",
        "columns": "H:I"
      },
      {
        "operation": "unhide_rows",
        "rows": "15"
      },
      {
        "operation": "unhide_columns",
        "columns": "H"
      }
    ]
  }
}
```

### Operaciones de ajuste automático
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/auto-sized.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "auto_fit_columns",
        "columns": "A:F"
      },
      {
        "operation": "auto_fit_rows",
        "rows": "1:20"
      }
    ]
  }
}
```

## Referencia de tipos de operaciones

### Operaciones de inserción
- `insert_rows` - Insertar filas nuevas en la posición especificada
- `insert_columns` - Insertar columnas nuevas en la posición especificada

### Operaciones de eliminación  
- `delete_rows` - Eliminar filas especificadas
- `delete_columns` - Eliminar columnas especificadas

### Operaciones de cambio de tamaño
- `set_row_height` - Establecer altura de fila específica en puntos
- `set_column_width` - Establecer ancho de columna específica en caracteres
- `auto_fit_rows` - Ajuste automático de filas al contenido en altura
- `auto_fit_columns` - Ajuste automático de columnas al contenido en ancho

### Operaciones de visibilidad
- `hide_rows` - Ocultar filas especificadas
- `unhide_rows` - Mostrar filas ocultas
- `hide_columns` - Ocultar columnas especificadas
- `unhide_columns` - Mostrar columnas ocultas

## Especificaciones de rango

### Rangos de filas
- `"1"` - Fila única (fila 1)
- `"1:3"` - Rango de filas (filas 1 a 3)
- `"5:10"` - Varias filas consecutivas

### Rangos de columnas
- `"A"` - Columna única (columna A)
- `"A:C"` - Rango de columnas (columnas A a C)
- `"D:F"` - Varias columnas consecutivas

## Ejemplos avanzados

### Configuración del encabezado del informe
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/header-setup.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "1:2",
        "height": 35
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 25
      },
      {
        "operation": "set_column_width",
        "columns": "B:E",
        "width": 12
      },
      {
        "operation": "set_column_width",
        "columns": "F",
        "width": 18
      }
    ]
  }
}
```

### Diseño de la tabla de datos
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/data-table.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "1",
        "count": 1
      },
      {
        "operation": "set_row_height",
        "rows": "1",
        "height": 25
      },
      {
        "operation": "auto_fit_columns",
        "columns": "A:J"
      },
      {
        "operation": "set_row_height",
        "rows": "2:100",
        "height": 18
      }
    ]
  }
}
```

### Diseño de presentación
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/presentation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "hide_columns",
        "columns": "B:C"
      },
      {
        "operation": "hide_rows",
        "rows": "10:15"
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 30
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      }
    ]
  }
}
```

## Guías de medición

### Alturas de fila (Puntos)
- `15` - Altura de fila predeterminada
- `20` - Un poco más alta para mejorar la legibilidad
- `25` - Bueno para encabezados
- `30` - Encabezados grandes
- `40` - Extragrande para títulos

### Ancho de columnas (Carácteres)
- `8` - Columnas estrechas (fechas, códigos)
- `12` - Columnas de datos estándar
- `15` - Columnas de texto medianas
- `20` - Columnas de texto anchas
- `25` - Extra anchas para descripciones
- `30` - Muy anchas para textos largos

## Mejores prácticas

1. **Tamaño del encabezado**: Haz que los encabezados sean más altos y anchos para mayor énfasis
2. **Consistencia de datos**: Usa alturas de fila consistentes para filas de datos
3. **Autoajustar**: Usa autoajuste para dimensionamiento dinámico del contenido
4. **Ocultar no usado**: Oculta filas/columnas vacías para una apariencia más limpia
5. **Agrupación lógica**: Agrupa operaciones de redimensionamiento relacionadas en lotes

## Patrones comunes

### Patrón de configuración de informes
1. Inserta filas de título en la parte superior
2. Establece la altura de la fila del encabezado
3. Ajustar automáticamente las columnas de datos
4. Establecer la altura estándar de las filas de datos
5. Ocultar áreas no utilizadas

### Patrón de Importación de Datos
1. Insertar filas para nuevos datos
2. Ajustar automáticamente las columnas al contenido
3. Estandarizar alturas de filas
4. Ocultar columnas de cálculo

### Patrón de Presentación
1. Ocultar filas/columnas de detalle
2. Ampliar áreas de resumen
3. Establecer dimensiones adecuadas para presentaciones
4. Mostrar solo datos relevantes

## Manejo de Errores

### Rango de filas inválido
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1", 
    "operation": "set_row_height",
    "rows": "0",
    "height": 20
  }
}
```
**Resultado**: Error - los números de fila comienzan desde 1

### Rango de columnas inválido
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_column_width", 
    "columns": "ZZ",
    "width": 10
  }
}
```
**Resultado**: Puede tener éxito pero fuera del uso típico

### Parámetros requeridos faltantes
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_row_height",
    "rows": "1"
  }
}
```
**Resultado**: Error - se requiere el parámetro de altura 
{{< app/cells/assistant language="nodejs-cpp" >}}

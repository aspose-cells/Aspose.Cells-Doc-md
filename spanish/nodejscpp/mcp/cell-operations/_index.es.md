---
title: Operaciones en celdas de Excel
linktitle: Operaciones en celdas
type: docs
weight: 60
url: /es/nodejs-cpp/mcp/cell-operations
keywords: "Operaciones en celdas de Excel, fusionar celdas de Excel, copiar y pegar en Excel, manipulación de celdas de Excel, operaciones en celdas de Excel con IA"
description: "Operaciones en celdas de Excel  fusionar, copiar/pegar, borrar celdas y manipulación avanzada de celdas con automatización de IA"
---

# Operaciones en celdas de Excel

Realiza operaciones avanzadas en **celdas de Excel** con automatización potenciada por IA. Fusiona celdas, realiza operaciones de copiar/pegar, borra contenido y manipula **celdas de Excel** con precisión.

## Herramientas disponibles

- `cell_operations` - **Operaciones en celdas de Excel** (fusionar, copiar/pegar, borrar) con automatización **potenciada por IA**
- `cell_operations_batch` - Realiza múltiples **operaciones en celdas de Excel** en lote mediante **MCP de hojas de cálculo**

## Operaciones en una sola celda

### Fusionar celdas
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/merged-layout.xlsx",
    "sheet_name": "Report",
    "operation": "merge_cells",
    "range": "A1:C1"
  }
}
```

### Desfusionar celdas
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/unmerged.xlsx",
    "sheet_name": "Data",
    "operation": "unmerge_cells",
    "range": "A1:C1"
  }
}
```

### Copiar celdas
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Source",
    "operation": "copy_cells",
    "source_range": "A1:D5"
  }
}
```

### Pegar solo valores
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Target",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```

### Borrar contenidos
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Data",
    "operation": "clear_contents",
    "range": "A1:Z100"
  }
}
```

## Operaciones de Celdas en Lote

### Flujo de trabajo de fusión y copiado completo
```json
{
  "tool": "cell_operations_batch", 
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A7:C7"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:F1",
        "destination_range": "A9"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F1", 
        "destination_range": "A12"
      }
    ]
  }
}
```

### Operaciones entre hojas
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet.xlsx",
    "sheet_name": "Summary",
    "operation": "paste_values",
    "source_range": "A1:F5",
    "source_sheet": "Data",
    "destination_range": "A1"
  }
}
```

### Operaciones de Limpieza de Datos
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/cleanup-demo.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "clear_contents",
        "range": "A1:A10"
      },
      {
        "operation": "clear_formats",
        "range": "B1:B10"
      },
      {
        "operation": "clear_all",
        "range": "C1:C10"
      }
    ]
  }
}
```

## Referencia de Tipos de Operaciones

### Operaciones de Fusión
- `merge_cells` - Fusionar celdas en una sola celda
- `unmerge_cells` - Dividir celdas fusionadas de nuevo en celdas individuales
- `merge_across` - Fusionar celdas a través de filas manteniendo filas separadas

### Operaciones de Copiar/Pegar
- `copy_cells` - Copiar rango de celdas al portapapeles
- `paste_values` - Pegado solo de valores (sin formato ni fórmulas)
- `paste_formulas` - Pegado solo de fórmulas (sin valores ni formato)
- `paste_formats` - Pegado solo de formato (sin valores ni fórmulas)
- `transpose_paste` - Pegado con orientación transpuesta (filas↔columnas)

### Operaciones de Borrado
- `clear_contents` - Borrar contenido de celdas (mantener formato)
- `clear_formats` - Borrar formato de celdas (mantener contenido)
- `clear_all` - Borrar tanto contenido como formato

## Ejemplos Avanzados

### Configuración del Título del Informe
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/title-report.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A1:F1"
      },
      {
        "operation": "merge_cells",
        "range": "A2:F2"
      },
      {
        "operation": "merge_cells",
        "range": "A3:C3"
      },
      {
        "operation": "merge_cells",
        "range": "D3:F3"
      }
    ]
  }
}
```

### Creación de Plantillas de Datos
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "templates/data-template.xlsx",
    "sheet_name": "Template",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F1"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A10"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A20"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A30"
      }
    ]
  }
}
```

### Consolidación de Datos
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/consolidated.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q1Data",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q2Data", 
        "destination_range": "A12"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q3Data",
        "destination_range": "A22"
      }
    ]
  }
}
```

### Separación de Fórmulas y Formatos
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/separated.xlsx",
    "sheet_name": "Analysis",
    "operations": [
      {
        "operation": "paste_formulas",
        "source_range": "A1:F10",
        "source_sheet": "Calculations",
        "destination_range": "A1"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F10", 
        "source_sheet": "Formatting",
        "destination_range": "A1"
      }
    ]
  }
}
```

## Operaciones Entre Hojas

### Copiar Entre Hojas
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet-copy.xlsx",
    "sheet_name": "Destination",
    "operation": "paste_values",
    "source_range": "A1:D10",
    "source_sheet": "Source",
    "destination_range": "B2"
  }
}
```

### Creación de Hoja Resumen
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/summary-creation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "January",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "February",
        "destination_range": "E2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "March",
        "destination_range": "I2"
      }
    ]
  }
}
```

## Transformación de Datos

### Transponer Datos
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/transposed.xlsx",
    "sheet_name": "Data",
    "operation": "transpose_paste",
    "source_range": "A1:E5",
    "destination_range": "G1"
  }
}
```

### Copiar Solo Valores
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/values-only.xlsx",
    "sheet_name": "Clean Data",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F20",
        "source_sheet": "Raw Data"
      },
      {
        "operation": "paste_values",
        "destination_range": "A1"
      }
    ]
  }
}
```

## Mejores Prácticas

1. **Combinar Estrategicamente**: Usa combinar para encabezados y títulos, no para áreas de datos
2. **Copiar Antes de Pegar**: Copia siempre el rango fuente antes de operaciones de pegar
3. **Limpiar Apropiadamente**: Escoge la operación de limpiar adecuada a tus necesidades
4. **Planificación entre Hojas**: Planifica operaciones en varias hojas para evitar conflictos
5. **Operaciones por Lotes**: Agrupa operaciones relacionadas para mejor rendimiento

## Casos de Uso Comunes

### Encabezados de Reporte
- Combinar celdas para títulos
- Copiar formato de encabezado
- Aplicar estilo consistente

### Limpieza de datos
- Eliminar contenido obsoleto
- Eliminar formato
- Restablecer estados de celdas

### Creación de plantillas
- Copiar patrones de formato
- Pegar estructura sin datos
- Crear diseños reutilizables

### Consolidación de datos
- Combinar datos de varias hojas
- Pegar solo valores para evitar conflictos con fórmulas
- Transponer orientación de datos

## Manejo de errores

### Rango de fusión inválido
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "merge_cells",
    "range": "A1"
  }
}
```
**Resultado**: Error - no se puede fusionar una sola celda

### Rango de origen faltante
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```
**Resultado**: Error - no hay datos copiados disponibles

### Referencia de hoja inválida
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "source_range": "A1:B2",
    "source_sheet": "NonExistentSheet",
    "destination_range": "A1"
  }
}
```
**Resultado**: Error - hoja de origen no encontrada 
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Formato de celda de Excel
linktitle: Formateo de celdas
type: docs
weight: 40
url: /es/nodejs-cpp/mcp/cell-formatting
keywords: "Formato de celdas de Excel, estilos de celdas de Excel, bordes de Excel, alineación de Excel, colores de fondo de Excel, formato de Excel con IA"
description: "Formato de celdas de Excel  aplicar fondos, bordes, alineación, formatos numéricos y estilos de celdas con automatización de IA"
---

# Formato de celdas de Excel

Aplicar formateo profesional **de celdas de Excel** con automatización potenciada por IA. Estiliza **las celdas de Excel** con fondos, bordes, alineación, formatos numéricos y propiedades avanzadas de las celdas.

## Herramientas disponibles

- `cell_format` - **Formato de celdas de Excel** (fondo, bordes, alineación, formato numérico) mediante **Excel MCP**
- `cell_format_batch` - Aplicar **formato de celdas de Excel** a múltiples rangos en lote con **automatización de IA**

## Formato de celda individual

### Estilo básico de celda
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/formatted-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "background_color": "#4472C4",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "text_wrap": true
  }
}
```

### Formato profesional de encabezados
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "range": "A1:F1",
    "background_color": "#2E5984",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "border_color": "#000000",
    "text_wrap": true
  }
}
```

### Formato numérico
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/financial.xlsx",
    "sheet_name": "Budget",
    "range": "C2:C10",
    "number_format": "$#,##0.00",
    "horizontal_align": "right"
  }
}
```

## Formato de celdas en lote

### Estilo completo del informe
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A1:F1",
        "background_color": "#2E5984",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "border_style": "thick",
        "border_color": "#000000"
      },
      {
        "range": "B2:B4",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "C2:C4",
        "number_format": "0",
        "horizontal_align": "center"
      },
      {
        "range": "D2:F5",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "A5:F5",
        "border_style": "thick",
        "border_sides": ["top"]
      }
    ]
  }
}
```

### Estilos avanzados de borde
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/border-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A5:A7",
        "border_style": "thin",
        "border_color": "#000000",
        "border_sides": ["all"]
      },
      {
        "range": "B5:B7",
        "border_style": "medium",
        "border_color": "#FF0000",
        "border_sides": ["outline"]
      },
      {
        "range": "C5:C7",
        "border_style": "dashed",
        "border_color": "#0000FF",
        "border_sides": ["top", "bottom"]
      },
      {
        "range": "D5:D7",
        "border_style": "dotted",
        "border_color": "#00FF00",
        "border_sides": ["left", "right"]
      },
      {
        "range": "E5:E7",
        "border_style": "double",
        "border_color": "#FF00FF",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Muestra de alineación de texto
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/alignment-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A10",
        "horizontal_align": "left",
        "vertical_align": "top",
        "background_color": "#FFE6E6"
      },
      {
        "range": "B10",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "background_color": "#E6FFE6"
      },
      {
        "range": "C10",
        "horizontal_align": "right",
        "vertical_align": "bottom",
        "background_color": "#E6E6FF"
      },
      {
        "range": "D10",
        "horizontal_align": "justify",
        "vertical_align": "justify",
        "text_wrap": true,
        "background_color": "#FFFFE6"
      },
      {
        "range": "E10",
        "horizontal_align": "fill",
        "indent": 2,
        "background_color": "#FFE6FF"
      }
    ]
  }
}
```

### Efectos de Rotación de Texto
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/rotation-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D1",
        "text_rotation": 45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "E1",
        "text_rotation": -45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "F1",
        "text_rotation": 90,
        "horizontal_align": "center",
        "vertical_align": "middle"
      }
    ]
  }
}
```

## Referencia de Parámetros de Formato

### Colores de Fondo
- `"#FFFFFF"` - Blanco
- `"#4472C4"` - Azul profesional
- `"#E6F3FF"` - Azul claro
- `"#FFFF00"` - Amarillo
- `"#FFE6E6"` - Rojo claro
- `"#E6FFE6"` - Verde claro
- `"#F0F8FF"` - Azul Alicia

### Alineación Horizontal
- `"left"` - Alineado a la izquierda
- `"center"` - Alineado al centro
- `"right"` - Alineado a la derecha
- `"justify"` - Justificado
- `"fill"` - Rellenar la celda

### Alineación Vertical
- `"top"` - Alineado en la parte superior
- `"middle"` - Alineado en el medio
- `"bottom"` - Alineado en la parte inferior
- `"justificar"` - Justificado verticalmente

### Estilos de borde
- `"ninguno"` - Sin borde
- `"delgado"` - Línea delgada
- `"medio"` - Línea mediana
- `"grueso"` - Línea gruesa
- `"-rayado"` - Línea discontinua
- `"punteado"` - Línea punteada
- `"doble"` - Línea doble

### Lados del borde
- `["todo"]` - Todos los lados
- `["arriba", "abajo"]` - Arriba y abajo
- `["izquierda", "derecha"]` - Izquierda y derecha
- `["contorno"]` - Solo bordes exteriores
- `["interior"]` - Solo bordes internos

### Formatos numéricos
- `"General"` - Formato predeterminado
- `"0"` - Entero
- `"0.00"` - Dos decimales
- `"0%"` - Porcentaje
- ``"$#,##0.00"`` - Moneda con separador de miles
- ``"yyyy-mm-dd"`` - Formato de fecha
- ``"h:mm AM/PM"`` - Formato de hora

### Propiedades de texto
- ``text_wrap: true`` - Ajustar texto en la celda
- ``text_rotation: 45`` - Rotar texto (grados)
- ``indent: 2`` - Indentar nivel de texto
- ``locked: true`` - Bloquear celda para protección
- ``hidden: true`` - Ocultar fórmula de celda

## Ejemplos avanzados de formato

### Estilo de informe financiero
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-complete.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D2:D5",
        "background_color": "#F0F8FF"
      },
      {
        "range": "E2:E5",
        "background_color": "#FFF0F0"
      },
      {
        "range": "F2:F5",
        "background_color": "#F0FFF0",
        "border_style": "double",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Resaltado de validación de datos
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/data-validation.xlsx",
    "sheet_name": "Data",
    "format_ranges": [
      {
        "range": "A2:A10",
        "background_color": "#90EE90"
      },
      {
        "range": "B2:B10",
        "background_color": "#FFB6C1"
      },
      {
        "range": "C2:C10",
        "background_color": "#87CEEB",
        "border_style": "thin",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Configuración de protección
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/protected.xlsx",
    "sheet_name": "Sheet1",
    "range": "B1:B5",
    "locked": false,
    "hidden": true
  }
}
```

## Mejores prácticas

1. **Armonía de colores**: Usa colores complementarios para una apariencia profesional
2. **Contraste**: Asegúrate de que el texto sea legible sobre los colores de fondo
3. **Consistencia**: Aplica un formato consistente en datos similares
4. ** Bordes**: Usa bordes para separar secciones y resaltar datos importantes
5. **Formatos numéricos**: Aplica formatos numéricos adecuados según los tipos de datos

## Casos de uso comunes

### Encabezados del Informe
- Fondo oscuro con texto blanco
- Alineación central
- Bordes gruesos
- Ajuste de texto activado

### Datos Financieros
- Formato de moneda
- Alineación a la derecha para números
- Resaltando valores negativos
- Separadores de miles

### Indicadores de Estado
- Fondos codificados por color
- Alineación central
- Bordes en negrita
- Distinción visual clara

### Tablas de Datos
- Colores alternos en filas
- Anchuras consistentes de columna
- Formatos numéricos adecuados
- Estilo de encabezado claro

## Manejo de errores

### Código de color inválido
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "background_color": "invalid-color"
  }
}
```
**Resultado**: Usa el color de fondo predeterminado

### Formato de número inválido
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "number_format": "invalid-format"
  }
}
```
**Resultado**: Usa el formato general como respaldo 
{{< app/cells/assistant language="nodejs-cpp" >}}

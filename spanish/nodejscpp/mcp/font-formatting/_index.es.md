---
title: Fuentes y Formato de Texto en Excel
linktitle: Fuente y Formato de Texto
type: docs
weight: 30
url: /es/nodejs-cpp/mcp/font-formatting
keywords: "Formato de fuente en Excel, Formato de texto en Excel, Configuración de fuente en Excel, Estilo de fuente AI en Excel, Automatización de fuentes en Excel"
description: "Formato de fuente y texto en Excel  aplicar estilos de fuente, colores, tamaños y efectos de texto con automatización AI"
---

# Formato de Fuente y Texto en Excel

Aplicar formateo profesional **de fuentes en Excel** con automatización impulsada por IA. Estilizar **texto en Excel** con fuentes, colores, tamaños y efectos especiales para hojas de cálculo pulidas.

## Herramientas disponibles

- `font_settings` - **Estilo de fuente en Excel** (familia, tamaño, negrita, cursiva, color, etc.) con **precisión de AI Excel**
- `font_settings_batch` - Aplicar **Configuración de fuente en Excel** a múltiples rangos en lote usando **spreadsheet MCP**

## Operaciones con fuente individual

### Estilo básico de fuente
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/styled-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "font_name": "Arial",
    "font_size": 14,
    "bold": true,
    "font_color": "#FFFFFF"
  }
}
```

### Efectos de texto
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/effects-demo.xlsx",
    "sheet_name": "Sheet1",
    "range": "A2",
    "italic": true,
    "underline": true,
    "strikethrough": true,
    "font_color": "#FF0000"
  }
}
```

### Caracteres especiales
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "range": "A3",
    "font_size": 10,
    "subscript": true
  }
}
```

## Operaciones en lote de fuente

### Estilo completo de encabezado
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/professional-report.xlsx",
    "sheet_name": "Summary Report",
    "font_ranges": [
      {
        "range": "C3:G3",
        "font_name": "Arial Black",
        "font_size": 16,
        "bold": true,
        "italic": true,
        "underline": true,
        "font_color": "#FF0000"
      },
      {
        "range": "D4:D6",
        "font_name": "Calibri",
        "font_size": 12,
        "bold": true,
        "font_color": "#0066CC"
      },
      {
        "range": "E4:E6",
        "font_name": "Times New Roman",
        "italic": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

### Demostración de efectos especiales de texto
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/text-effects.xlsx",
    "sheet_name": "Effects Demo",
    "font_ranges": [
      {
        "range": "A3",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "B3",
        "font_size": 10,
        "superscript": true
      },
      {
        "range": "C3",
        "strikethrough": true,
        "underline": true,
        "font_color": "#CC0000"
      }
    ]
  }
}
```

### Estilo profesional de informes
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "font_ranges": [
      {
        "range": "A1:F1",
        "font_name": "Arial",
        "font_size": 14,
        "bold": true,
        "font_color": "#FFFFFF"
      },
      {
        "range": "A5:F5",
        "bold": true,
        "font_size": 12
      },
      {
        "range": "F2:F5",
        "bold": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

## Referencia de parámetros de fuente

### Familias de fuentes
- `"Arial"` - Sin-serif limpia y moderna
- `"Calibri"` - Valor predeterminado de Microsoft Office
- `"Times New Roman"` - Serif tradicional
- `"Arial Black"` - Fuente en negrita para pantallas
- `"Courier New"` - Fuente monoespaciada

### Tamaños de fuente
- `8` - Texto muy pequeño
- `10` - Texto pequeño
- `11` - Tamaño predeterminado
- `12` - Texto de cuerpo estándar
- `14` - Texto grande
- `16` - Tamaño de encabezado
- `18` - Encabezado grande

### Colores de fuente (Códigos Hex)
- `"#000000"` - Negro
- `"#FFFFFF"` - Blanco
- `"#FF0000"` - Rojo
- `"#0066CC"` - Azul
- `"#006600"` - Verde
- `"#FF6600"` - Naranja
- `"#800080"` - Púrpura

### Efectos de texto
- `bold: true` - Texto en negrita
- `italic: true` - Texto en cursiva
- `underline: true` - Texto subrayado
- `strikethrough: true` - Texto tachado
- `subscript: true` - Texto con subíndice (H₂O)
- `superscript: true` - Texto con superíndice (x²)

## Estilo avanzado de fuente

### Ejemplo de notación científica
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "font_ranges": [
      {
        "range": "A1",
        "font_name": "Times New Roman",
        "font_size": 12,
        "bold": true
      },
      {
        "range": "B1",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "C1",
        "font_size": 10,
        "superscript": true
      }
    ]
  }
}
```

### Datos codificados por colores
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/color-coded.xlsx",
    "sheet_name": "Status Report",
    "font_ranges": [
      {
        "range": "A2:A5",
        "font_color": "#008000",
        "bold": true
      },
      {
        "range": "B2:B5",
        "font_color": "#FF8C00",
        "italic": true
      },
      {
        "range": "C2:C5",
        "font_color": "#DC143C",
        "strikethrough": true
      }
    ]
  }
}
```

## Mejores prácticas

1. **Consistencia**: Usa familias de fuentes coherentes en todos los informes
2. **Jerarquía**: Usa tamaños de fuente para crear jerarquía visual
3. **Legibilidad**: Asegura suficiente contraste entre texto y fondo
4. **Efectos**: Usa efectos de texto con moderación para énfasis
5. **Profesionalismo**: Usa fuentes estándar para informes comerciales

## Casos de uso comunes

### Encabezados de informes
- Fuente en negrita y tamaño mayor
- Colores contrastantes
- Familias de fuentes profesionales

### Énfasis en datos
- En negrita o cursiva para valores importantes
- Codificación por colores para indicadores de estado
- Tachado para datos obsoletos

### Documentos científicos
- Subíndice para fórmulas químicas
- Superíndice para expresiones matemáticas
- Monoespaciado para código o datos

## Manejo de errores

### Familia de fuentes no válida
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_name": "NonExistentFont"
  }
}
```
**Resultado**: Se vuelve a la fuente predeterminada del sistema

### Código de color no válido
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_color": "invalid-color"
  }
}
```
**Resultado**: Usa el color negro predeterminado 
{{< app/cells/assistant language="nodejs-cpp" >}}

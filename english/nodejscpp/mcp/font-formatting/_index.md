---
title: Excel Font and Text Formatting
linktitle: Font and Text Formatting
type: docs
weight: 30
url: /nodejs-cpp/mcp/font-formatting
keywords: "Excel font formatting, Excel text formatting, Excel font settings, AI Excel font styling, Excel font automation"
description: "Excel font and text formatting - apply font styles, colors, sizes, and text effects with AI automation"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Font and Text Formatting

Apply professional **Excel font formatting** with AI‑powered automation. Style **Excel text** with fonts, colors, sizes, and special effects for polished spreadsheets.

## Available Tools

- `font_settings` – **Excel font styling** (family, size, bold, italic, color, etc.) with **AI Excel** precision  
- `font_settings_batch` – Apply **Excel font settings** to multiple ranges in batch using **spreadsheet MCP**

## Single Font Operations

### Basic Font Styling
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

### Text Effects
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

### Special Characters
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

## Batch Font Operations

### Complete Header Styling
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

### Special Text Effects Showcase
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

### Professional Report Styling
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

## Font Parameters Reference

### Font Families
- `"Arial"` – Clean, modern sans‑serif  
- `"Calibri"` – Microsoft Office default  
- `"Times New Roman"` – Traditional serif  
- `"Arial Black"` – Bold display font  
- `"Courier New"` – Monospace font  

### Font Sizes
- `8` – Very small text  
- `10` – Small text  
- `11` – Default size  
- `12` – Standard body text  
- `14` – Large text  
- `16` – Heading size  
- `18` – Large heading  

### Font Colors (Hex Codes)
- `"#000000"` – Black  
- `"#FFFFFF"` – White  
- `"#FF0000"` – Red  
- `"#0066CC"` – Blue  
- `"#006600"` – Green  
- `"#FF6600"` – Orange  
- `"#800080"` – Purple  

### Text Effects
- `bold: true` – Bold text  
- `italic: true` – Italic text  
- `underline: true` – Underlined text  
- `strikethrough: true` – Strikethrough text  
- `subscript: true` – Subscript text (H₂O)  
- `superscript: true` – Superscript text (x²)  

## Advanced Font Styling

### Scientific Notation Example
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

### Color‑Coded Data
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

## Best Practices

1. **Consistency** – Use consistent font families throughout reports.  
2. **Hierarchy** – Use font sizes to create visual hierarchy.  
3. **Readability** – Ensure adequate contrast between text and background.  
4. **Effects** – Use text effects sparingly for emphasis.  
5. **Professional** – Stick to standard business fonts for reports.  

## Common Use Cases

### Report Headers
- Bold, larger font size  
- Contrasting colors  
- Professional font families  

### Data Emphasis
- Bold or italic for important values  
- Color coding for status indicators  
- Strikethrough for deprecated data  

### Scientific Documents
- Subscript for chemical formulas  
- Superscript for mathematical expressions  
- Monospace for code or data  

## Error Handling

### Invalid Font Family
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
**Result**: Falls back to the default system font.

### Invalid Color Code
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
**Result**: Uses the default black color.  

{{< app/cells/assistant language="nodejs-cpp" >}}

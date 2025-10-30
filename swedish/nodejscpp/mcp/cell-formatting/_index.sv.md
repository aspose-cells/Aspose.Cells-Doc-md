---
title: Excel Cellformatering
linktitle: Cellformatering
type: docs
weight: 40
url: /sv/nodejs-cpp/mcp/cell-formatting
keywords: "Excel cellformatering, Excel cellstilar, Excel gränser, Excel justering, Excel bakgrundsfärger, AI Excel formatering"
description: "Excel cellformatering  applicera bakgrunder, gränser, justering, sifferformat och cellstilar med AI automatisering"
---

# Excel Cellformatering

Använd professionell **Excel cellformatering** med AI-drivna automatisering. Stil **Excel celler** med bakgrunder, gränser, justering, sifferformat och avancerade cellegenskaper.

## Tillgängliga Verktyg

- `cell_format` - **Excel cellformatering** (bakgrund, gränser, justering, sifferformat) via **Excel MCP**
- `cell_format_batch` - Tillämpa **Excel cellformatering** på flera områden i batch med **AI-automatisering**

## Enkel cellformatering

### Grundläggande cellstilering
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

### Professionell rubrikformatering
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

### Nummerformat
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

## Batch cellformatering

### Komplett rapportstilning
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

### Avancerade gränsstilar
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

### Textjustering Showcase
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

### Textrotationseffekter
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

## Referens för formateringsparametrar

### Bakgrundsfärger
- `"#FFFFFF"` - Vitt
- `"#4472C4"` - Professionell blå
- `"#E6F3FF"` - Ljusblå
- `"#FFFF00"` - Gul
- `"#FFE6E6"` - Ljusröd
- `"#E6FFE6"` - Ljusgrön
- `"#F0F8FF"` - Alice blå

### Horizontell inriktning
- `"left"` - Vänsterjusterad
- `"center"` - CEntrerjusterad
- `"right"` - Högerjusterad
- `"justify"` - Marginaljusterad
- `"fill"` - Fyll cellen

### Vertikal inriktning
- `"top"` - Toppjusterad
- `"middle"` - Mittenjusterad
- `"bottom"` - Bottenjusterad
- `"justify"` - Justify vertikalt

### Borderstilar
- `"none"` - Ingen kant
- `"thin"` - Tunn linje
- `"medium"` - Medelstort linje
- `"thick"` - Tjock linje
- `"dashed"` - Streckad linje
- `"dotted"` - Prickad linje
- `"double"` - Dubbel linje

### Kantlinjer
- `["all"]` - Alla sidor
- `["top", "bottom"]` - Top och botten
- `["left", "right"]` - Vänster och höger
- `["outline"]` - Endast ytterkantlinjer
- `["inside"]` - Endast innerkantlinjer

### Numformat
- `"General"` - Standardformat
- `"0"` - Heltal
- `"0.00"` - Två decimaler
- `"0%"` - Procent
- `"$#,##0.00"` - Valuta med tusentalsavgränsare
- `"yyyy-mm-dd"` - Datumformat
- `"h:mm AM/PM"` - Tidsformat

### Textegenskaper
- `text_wrap: true` - Textbrytning i cell
- `text_rotation: 45` - Rotera text (grader)
- `indent: 2` - Indentera textnivå
- `locked: true` - Lås cell för skydd
- `hidden: true` - Dölj cellformel

## Avancerade formateringsexempel

### Finansiell rapportstil
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

### Datavalideringsmarkering
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

### Skyddsinställningar
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

## Bästa praxis

1. **Färgharmoni**: Använd kompletterande färger för ett professionellt utseende
2. **Kontrast**: Se till att texten är lättläst mot bakgrundsfärger
3. **Konsistens**: Använd konsekvent formatering för liknande data
4. **Gränser**: Använd gränser för att separera sektioner och lyfta fram viktig data
5. **Nummerformat**: Använd lämpliga nummerformat för datatyper

## Vanliga användningsområden

### Rapportrubriker
- Mörk bakgrund med vit text
- Centrerad justering
- Tjocka ramar
- Textombrott aktiverat

### Ekonomisk data
- Valutformat
- Högerjustering för siffror
- Markering av negativa värden
- Tusentalsseparatorer

### Statusindikatorer
- Färgcodade bakgrunder
- Centrerad justering
- Fetade ramar
- Tydlig visuell skillnad

### Databord
- Alternativa radfärger
- Konsekventa kolumnbredder
- Passande numberformat
- Tydlig header-styling

## Felhantering

### Ogiltig färgkod
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
**Resultat**: Använder standardbakgrundsfärgen

### Ogiltigt nummersformat
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
**Resultat**: Använder allmänt format som fallback 
{{< app/cells/assistant language="nodejs-cpp" >}}

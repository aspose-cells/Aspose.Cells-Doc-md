---
title: Formattazione celle Excel
linktitle: Formattazione celle
type: docs
weight: 40
url: /it/nodejs-cpp/mcp/cell-formatting
keywords: "Formattazione celle Excel, Stili celle Excel, Bordi Excel, Allineamento Excel, Colori di sfondo Excel, Formattazione AI Excel"
description: "Formattazione celle Excel  applica sfondi, bordi, allineamento, formati numerici e stili celle con automazione AI"
---

# Formattazione celle Excel

Applica una **formattazione celle Excel** professionale con automazione basata su IA. Stila le **celle Excel** con sfondi, bordi, allineamenti, formati numerici e proprietà avanzate delle celle.

## Strumenti disponibili

- `cell_format` - **formattazione celle Excel** (sfondo, bordi, allineamento, formato numerico) tramite **Excel MCP**
- `cell_format_batch` - Applica **formattazione celle Excel** a più intervalli in batch con **automazione AI**

## Formattazione singola cella

### Stile di base delle celle
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

### Formattazione professionale dell'intestazione
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

### Formattazione dei numeri
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

## Formattazione batch delle celle

### Stile di report completo
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

### Stili avanzati dei bordi
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

### Mostra allineamento del testo
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

### Effetti di Rotazione del Testo
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

## Riferimento ai Parametri di Formattazione

### Colori di Sfondo
- `"#FFFFFF"` - Bianco
- `"#4472C4"` - Blu professionale
- `"#E6F3FF"` - Blue chiaro
- `"#FFFF00"` - Giallo
- `"#FFE6E6"` - Rosso chiaro
- `"#E6FFE6"` - Verde chiaro
- `"#F0F8FF"` - Blu Alice

### Allineamento Orizzontale
- `"left"` - Allineato a sinistra
- `"center"` - Centrare
- `"right"` - Allineato a destra
- `"justify"` - Giustificato
- `"fill"` - Riempi la cella

### Allineamento Verticale
- `"top"` - Allineato in alto
- `"middle"` - Allineato al centro
- `"bottom"` - Allineato in basso
- `"justify"` - Giustificato verticalmente

### Stili del bordo
- `"none"` - Nessun bordo
- `"thin"` - Linea sottile
- `"medium"` - Linea media
- `"thick"` - Linea spessa
- `"dashed"` - Linea tratteggiata
- `"dotted"` - Linea punteggiata
- `"double"` - Linea doppia

### Lati del bordo
- `["tutto"]` - Tutti i lati
- `["alto", "basso"]` - Alto e basso
- `["sinistra", "destra"]` - Sinistra e destra
- `["contorno"]` - Solo i confini esterni
- `["interno"]` - Solo i confini interni

### Formati numerici
- `"Generale"` - Formato predefinito
- `"0"` - Numero intero
- `"0.00"` - Due decimali
- `"0%"` - Percentuale
- `"$#,##0.00"` - Valuta con separatore delle migliaia
- `"yyyy-mm-dd"` - Formato data
- `"h:mm AM/PM"` - Formato orario

### Proprietà del testo
- `text_wrap: true` - Avvolgi testo nella cella
- `text_rotation: 45` - Ruota testo (gradi)
- `indent: 2` - Rientra livello di testo
- `locked: true` - Blocca la cella per protezione
- `hidden: true` - Nascondi formula della cella

## Esempi di formattazione avanzata

### Stile del rapporto finanziario
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

### Evidenziazione con convalida dati
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

### Impostazioni di protezione
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

## Buone pratiche

1. **Armonia dei colori**: Usa colori complementari per un aspetto professionale
2. **Contrasto**: Assicurati che il testo sia leggibile contro i colori di sfondo
3. **Coerenza**: Applica formattazioni coerenti su dati simili
4. **Bordi**: Usa bordi per separare le sezioni e evidenziare dati importanti
5. **Formati numerici**: Applica formati numerici appropriati per tipi di dati

## Casi d'uso comuni

### Intestazioni del rapporto
- Sfondo scuro con testo bianco
- Allineamento centrale
-Bordi spessi
- Testo avvolgente abilitato

### Dati finanziari
- Formattazione valuta
- Allineamento a destra per i numeri
- Evidenziare valori negativi
- Separatori delle migliaia

### Indicatori di stato
- Sfondi colorati
- Allineamento centrale
- Bordi in grassetto
- Chiarezza nella distinzione visiva

### Tabelle dei dati
- Colori delle righe alternate
- Larghezze delle colonne coerenti
- Formati numerici appropriati
- Stilizzazione chiara dell'intestazione

## Gestione degli errori

### Codice colore non valido
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
**Risultato**: Usa il colore di sfondo predefinito

### Formato numerico non valido
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
**Risultato**: Usa il formato Generale come fallback 
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Font e formattazione del testo in Excel
linktitle: Font e formattazione del testo
type: docs
weight: 30
url: /it/nodejs-cpp/mcp/font-formatting
keywords: "Formattazione font in Excel, formattazione testo in Excel, impostazioni font in Excel, stile font AI in Excel, automazione font in Excel"
description: "Formattazione font e testo in Excel  applica stili di font, colori, dimensioni ed effetti speciali con automazione AI"
---

# Font e formattazione del testo in Excel

Applica una formattazione professionale **font in Excel** con automazione alimentata da AI. Stila **testo in Excel** con font, colori, dimensioni ed effetti speciali per fogli di calcolo raffinati.

## Strumenti disponibili

- `font_settings` - **Stile del carattere di Excel** (famiglia, dimensione, grassetto, corsivo, colore, ecc.) con **AI Excel** di precisione
- `font_settings_batch` - Applica **impostazioni del carattere di Excel** a più intervalli in batch usando **spreadsheet MCP**

## Operazioni singole sul carattere

### Stile di carattere di base
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

### Effetti del testo
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

### Caratteri speciali
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

## Operazioni di batch sul carattere

### Stile completo dell'intestazione
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

### Vetrina di effetti speciali del testo
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

### Stile del rapporto professionale
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

## Riferimento ai parametri del carattere

### Famiglie di caratteri
- `"Arial"` - Pulito, moderno senza grazie
- `"Calibri"` - Default di Microsoft Office
- `"Times New Roman"` - Tradizionale con grazie
- `"Arial Black"` - Font in grassetto per visualizzazione
- `"Courier New"` - Font monospazio

### Dimensioni del carattere
- `8` - Testo molto piccolo
- `10` - Testo piccolo
- `11` - Dimensione predefinita
- `12` - Testo normale di corpo
- `14` - Testo grande
- `16` - Dimensione intestazione
- `18` - Grande intestazione

### Colori del font (Codici Hex)
- `"#000000"` - Nero
- `"#FFFFFF"` - Bianco
- `"#FF0000"` - Rosso
- `"#0066CC"` - Blu
- `"#006600"` - Verde
- `"#FF6600"` - Arancione
- `"#800080"` - Viola

### Effetti del testo
- `bold: true` - Testo in grassetto
- `italic: true` - Testo in corsivo
- `underline: true` - Testo sottolineato
- `strikethrough: true` - Testo barrato
- `subscript: true` - Testo in apice (H₂O)
- `superscript: true` - Testo in apice (x²)

## Stilizzazione avanzata dei caratteri

### Esempio di notazione scientifica
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

### Dati codificati a colore
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

## Le migliori pratiche

1. **Coerenza**: Usa Famiglie di caratteri coerenti in tutti i rapporti
2. **Gerarchia**: Usa le dimensioni dei caratteri per creare gerarchie visive
3. **Leggibilità**: Garantire un contrasto adeguato tra testo e sfondo
4. **Effetti**: Usa gli effetti del testo con parsimonia per enfasi
5. **Professionale**: Attenersi ai caratteri standard aziendali per i rapporti

## Casi d'uso comuni

### Intestazioni dei report
- Carattere in grassetto, dimensione maggiore
- Colori contrastanti
- Famiglie di caratteri professionali

### Enfasi sui dati
- Grassetto o corsivo per valori importanti
- Codifica colore per indicatori di stato
- Barrato per dati obsoleti

### Documenti scientifici
- Pedice per formule chimiche
- Apice per espressioni matematiche
- Monospazio per codice o dati

## Gestione degli errori

### Font Family non valida
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
**Risultato**: Ricade sul font di sistema predefinito

### Codice colore non valido
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
**Risultato**: Usa il colore nero di default 
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Operazioni con le celle di Excel
linktitle: Operazioni con le celle
type: docs
weight: 60
url: /it/nodejs-cpp/mcp/cell-operations
keywords: "Operazioni con le celle di Excel, unisci celle di Excel, copia e incolla in Excel, manipolazione delle celle di Excel, operazioni con le celle di Excel AI"
description: "Operazioni con le celle di Excel  unisci, copia/incolla, cancella celle e manipolazione avanzata delle celle con automazione AI"
---

# Operazioni con le celle di Excel

Esegui operazioni avanzate **con le celle di Excel** con automazione alimentata da AI. Unisci celle, operazioni di copia/incolla, cancella contenuti e manipola **celle di Excel** con precisione.

## Strumenti disponibili

- `cell_operations` - **Operazioni con le celle di Excel** (unisci, copia/incolla, cancella) con automazione **alimentata da AI**
- `cell_operations_batch` - Esegui più **operazioni con le celle di Excel** in batch tramite **spreadsheet MCP**

## Operazioni singole con le celle

### Unisci celle
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

### Disunisci celle
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

### Copia celle
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

### Incolla valori
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

### Cancella contenuti
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

## Operazioni di Celle in Blocco

### Flusso di lavoro Completo di Unione e Copy
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

### Operazioni Trasversali tra Fogli
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

### Operazioni di Pulizia dei Dati
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

## Riferimento sui Tipi di Operazioni

### Operazioni di Unione
- `merge_cells` - Unisci le celle in una singola cella
- `unmerge_cells` - Dividi le celle unite in celle singole
- `merge_across` - Unisci le celle attraverso le righe mantenendo righe separate

### Operazioni di Copia/Incolla
- `copy_cells` - Copia l'intervallo di celle negli appunti
- `paste_values` - Incolla solo i valori (senza formattazione o formule)
- `paste_formulas` - Incolla solo le formule (senza valori o formattazione)
- `paste_formats` - Incolla solo la formattazione (senza valori o formule)
- `transpose_paste` - Incolla con orientamento trasposto (righe↔colonne)

### Operazioni di Cancellazione
- `clear_contents` - Cancella contenuto delle celle (mantieni la formattazione)
- `clear_formats` - Cancella la formattazione delle celle (mantieni i contenuti)
- `clear_all` - Cancella sia contenuti che formattazione

## Esempi Avanzati

### Configurazione del titolo del rapporto
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

### Creazione del modello di dati
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

### Consolidamento dei dati
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

### Separazione di formule e formattazione
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

## Operazioni tra fogli

### Copia tra fogli
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

### Creazione di fogli di riepilogo
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

## Trasformazione dei dati

### Trasporre i dati
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

### Copia solo valori
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

## Buone pratiche

1. **Unisci strategicamente**: Utilizza l'unione per intestazioni e titoli, non per le aree di dati
2. **Copia prima di incollare**: Copia sempre l'intervallo di origine prima di operazioni di incolla
3. **Pulisci in modo appropriato**: Scegli l'operazione di pulizia adatta alle tue esigenze
4. **Pianificazione tra fogli**: Pianifica le operazioni multi-foglio per evitare conflitti
5. **Operazioni batch**: Raggruppa le operazioni correlate per migliorare le prestazioni

## Casi d'uso comuni

### Intestazioni del rapporto
- Unisci le celle per i titoli
- Copia la formattazione dell'intestazione
- Applicare uno stile coerente

### Pulizia dati
- Eliminare contenuto obsoleto
- Rimuovere formattazione
- Resettare gli stati delle celle

### Creazione di modelli
- Copiare schemi di formattazione
- Incollare struttura senza dati
- Creare layout riutilizzabili

### Consolidamento dati
- Combinare dati da più fogli
- Incollare solo valori per evitare conflitti di formule
- Trasporre l’orientamento dei dati

## Gestione degli errori

### Intervallo di unione non valido
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
**Risultato**: Errore - impossibile unire singola cella

### Intervallo di origine mancante
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
**Risultato**: Errore - nessun dato copiato disponibile

### Riferimento foglio non valido
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
**Risultato**: Errore - foglio di origine non trovato 
{{< app/cells/assistant language="nodejs-cpp" >}}

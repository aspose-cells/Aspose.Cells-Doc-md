---
title: Operazioni su righe e colonne di Excel
linktitle: Operazioni su righe e colonne
type: docs
weight: 50
url: /it/nodejs-cpp/mcp/row-column-operations
keywords: "Operazioni su righe di Excel, operazioni su colonne di Excel, gestione layout di Excel, inserimento righe, eliminazione colonne, ridimensionamento celle di Excel"
description: "Operazioni su righe e colonne di Excel  inserisci, elimina, ridimensiona, nascondi/riprendi righe e colonne con automazione AI"
---

# Operazioni su righe e colonne di Excel

Gestisci le **operazioni su righe e colonne di Excel** con automazione alimentata da AI. Inserisci, elimina, ridimensiona, nascondi/riprendi **righe** e **colonne** di Excel per una gestione perfetta del layout del foglio di calcolo.

## Strumenti disponibili

- `row_column_operations` - **Operazioni su righe e colonne di Excel** (inserisci, elimina, ridimensiona, nascondi/riprendi) con **AI Excel**
- `row_column_operations_batch` - Esegui più **operazioni su righe e colonne di Excel** in batch usando **Excel MCP**

## Operazioni singole

### Inserisci righe
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

### Elimina colonne
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

### Imposta altezza riga
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

### Imposta larghezza colonna
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

## Operazioni batch

### Configurazione layout completa
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

### Operazioni di inserimento e cancellazione
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

### Operazioni di nascondere e rendere visibile
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

### Operazioni di adattamento automatico
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

## Riferimento ai tipi di operazione

### Operazioni di inserimento
- `insert_rows` - Inserisci nuove righe alla posizione specificata
- `insert_columns` - Inserisci nuove colonne alla posizione specificata

### Operazioni di cancellazione  
- `delete_rows` - Elimina righe specificate
- `delete_columns` - Elimina colonne specificate

### Operazioni di ridimensionamento
- `set_row_height` - Imposta altezza riga specifica in punti
- `set_column_width` - Imposta larghezza colonna specifica in caratteri
- `auto_fit_rows` - Adatta automaticamente le righe all'altezza del contenuto
- `auto_fit_columns` - Adatta automaticamente le colonne alla larghezza del contenuto

### Operazioni di visibilità
- `hide_rows` - Nascondi righe specificate
- `unhide_rows` - Mostra righe nascoste
- `hide_columns` - Nascondi colonne specificate
- `unhide_columns` - Mostra colonne nascoste

## Specifiche dell'intervallo

### Intervalli di Righe
- `"1"` - Riga singola (riga 1)
- `"1:3"` - Intervallo di righe (righe da 1 a 3)
- `"5:10"` - Multiple righe consecutive

### Intervalli di Colonne
- `"A"` - Colonna singola (colonna A)
- `"A:C"` - Intervallo di colonne (colonne A a C)
- `"D:F"` - Multiple colonne consecutive

## Esempi Avanzati

### Configurazione dell'intestazione del report
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

### Layout della tabella dati
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

### Layout della presentazione
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

## Linee guida di misurazione

### Altezza delle righe (Punti)
- `15` - Altezza predefinita della riga
- `20` - Leggermente più alta per una maggiore leggibilità
- `25` - Buono per intestazioni
- `30` - Intestazioni grandi
- `40` - Extra large per titoli

### Larghezze delle Colonne (Caratteri)
- `8` - Colonne strette (date, codici)
- `12` - Colonne dati standard
- `15` - Colonne di testo medie
- `20` - Colonne di testo larghe
- `25` - Extra larghe per descrizioni
- `30` - Molto larghe per testi lunghi

## Buone Pratiche

1. **Dimensione Intestazione**: Rendere le intestazioni più alte e larghe per maggior risalto
2. **Coerenza dei Dati**: Utilizzare altezze di riga coerenti per le righe dei dati
3. **Auto-adeguamento**: Utilizzare l'auto-adeguamento per dimensionare il contenuto dinamico
4. **Nascondi Non Usati**: Nascondere righe/colonne vuote per un aspetto più pulito
5. **Raggruppamento Logico**: Raggruppare le operazioni di resizing correlate in batch

## Pattern Comuni

### Pattern di Configurazione del Rapporto
1. Inserire righe di titolo in cima
2. Impostare l'altezza della riga di intestazione
3. Adatta automaticamente le colonne dei dati
4. Imposta un'altezza standard per le righe dei dati
5. Nascondi le aree inutilizzate

### Pattern di Importazione Dati
1. Inserisci righe per nuovi dati
2. Adatta automaticamente le colonne al contenuto
3. Standardizza le altezze delle righe
4. Nascondi le colonne di calcolo

### Pattern di Presentazione
1. Nascondi le righe/colonne di dettaglio
2. Ingrandisci le aree di riepilogo
3. Imposta dimensioni adatte alla presentazione
4. Mostra solo i dati pertinenti

## Gestione Errori

### Intervallo di righe non valido
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
**Risultato**: Errore - i numeri di riga partono da 1

### Intervallo di colonne non valido
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
**Risultato**: Può riuscire ma oltre l'uso tipico

### Parametri obbligatori mancanti
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
**Risultato**: Errore - parametro altezza richiesto 
{{< app/cells/assistant language="nodejs-cpp" >}}

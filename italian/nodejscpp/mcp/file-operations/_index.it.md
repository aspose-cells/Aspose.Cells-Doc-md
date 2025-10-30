---
title: File Excel e Operazioni sui Dati
linktitle: File e Operazioni sui Dati
type: docs
weight: 10
url: /it/nodejs-cpp/mcp/file-operations
keywords: "Operazioni sui file Excel, operazioni sui dati Excel, crea cartelle di lavoro Excel, foglio di lavoro Excel, leggi dati Excel, scrivi dati Excel"
description: "Operazioni sui file e dati Excel  crea cartelle di lavoro, gestisci fogli di lavoro, leggi e scrivi dati Excel con automazione AI"
---

# File Excel e Operazioni sui Dati

Gestisci **File Excel** e **operazioni sui dati** con automazione potenziata dall'IA. Crea **Cartelle di lavoro Excel**, gestisci **fogli di lavoro** e esegui operazioni di **lettura/scrittura dati Excel**.

## Strumenti Disponibili

- `create_workbook` - Crea nuove **cartelle di lavoro Excel** con automazione **AI Excel**
- `create_worksheet` - Aggiungi **fogli di lavoro Excel** alle **cartelle di lavoro Excel** esistenti
- `get_workbook_info` - Ottieni metadati e informazioni sulla **cartella di lavoro Excel**
- `read_data_from_excel` - Leggi dati dai **fogli di lavoro Excel** con precisione **potenziata dall'IA**
- `write_data_to_excel` - Scrivi dati nei **fogli di lavoro Excel** tramite **Excel MCP**

## Crea Cartelle di Lavoro Excel

### Crea Cartella di Lavoro Base
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### Crea Cartella di Lavoro con Foglio Personalizzato
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## Gestisci Fogli di Lavoro

### Aggiungi Nuovo Foglio di Lavoro
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### Ottieni Informazioni sulla Cartella di Lavoro
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Scrivi Dati Excel

### Scrivi Intestazioni e Dati
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### Scrivi dati nella posizione personalizzata
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## Leggi dati da Excel

### Leggi intervallo completo utilizzato
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### Leggi intervallo specifico
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### Leggi dalla posizione predefinita
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## Esempio di workflow completo

### 1. Crea il tuo primo report Excel
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. Aggiungi foglio di riepilogo
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. Scrivi dati di vendita
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. Verifica i dati
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. Controlla la struttura del workbook
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## Buone pratiche

1. **Percorsi dei file**: utilizza percorsi relativi per una migliore portabilità
2. **Nomi dei fogli**: usa nomi descrittivi per i fogli di lavoro
3. **Struttura dei dati**: organizza i dati con intestazioni chiare
4. **Lettura di intervalli**: specifica intervalli per grandi set di dati
5. **Gestione degli errori**: verifica l'esistenza del file prima delle operazioni

## Pattern comuni

### Pattern di importazione dati
1. Crea un workbook
2. Scrivi dati grezzi
3. Leggi per verificare
4. Elabora con formule

### Rapporti Multi-Foglio
1. Crea cartella di lavoro con foglio principale
2. Aggiungi fogli di riepilogo/analisi
3. Scrivi dati in ogni foglio
4. Collega i fogli con formule

### Validazione dei Dati
1. Scrivi dati
2. Leggi indietro intervalli specifici
3. Verifica l'integrità dei dati
4. Gestisci valori mancanti 
{{< app/cells/assistant language="nodejs-cpp" >}}

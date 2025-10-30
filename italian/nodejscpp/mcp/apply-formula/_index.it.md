---
title: Operazioni con formule Excel  MCP di formula Excel
linktitle: Operazioni formule  Formule Excel MCP
type: docs
weight: 20
url: /it/nodejs-cpp/mcp/apply-formula
keywords: "Formule Excel MCP, formule Excel, formule AI Excel, automazione formule Excel, calcoli Excel"
description: "Formule Excel MCP  Applica formule Excel con automazione AI, operazioni su singole celle e batch"
---

# Operazioni formule Excel

**Excel Formula MCP** fornisce potente automazione delle **formule Excel** con integrazione AI. Applica **formule Excel** a celle singole o multiple in operazioni batch.

## Strumenti disponibili

- `apply_formula` - Applica **formule Excel** a celle singole con **Excel Formula MCP**
- `apply_formula_batch` - Applica **formule Excel** a più celle in batch usando **AI Excel**

## Operazioni formula singola

### Applica formula con segno di uguale
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/calculations.xlsx",
    "sheet_name": "Data",
    "cell": "D2",
    "formula": "=B2*C2"
  }
}
```

### Applica formula senza segno di uguale
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/calculations.xlsx",
    "sheet_name": "Data",
    "cell": "E2",
    "formula": "SUM(B2:D2)"
  }
}
```

### Formule Excel comuni
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Summary",
    "cell": "F2",
    "formula": "=AVERAGE(A2:E2)"
  }
}
```

## Operazioni formula batch

### Calcola totali del rapporto di vendita
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "formulas": [
      { "cell": "E2", "formula": "=C2*D2" },
      { "cell": "E3", "formula": "=C3*D3" },
      { "cell": "E4", "formula": "=C4*D4" },
      { "cell": "E5", "formula": "=SUM(E2:E4)" }
    ]
  }
}
```

### Rapporto finanziario con calcoli fiscali
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "formulas": [
      { "cell": "D2", "formula": "=B2*C2" },
      { "cell": "D3", "formula": "=B3*C3" },
      { "cell": "D4", "formula": "=B4*C4" },
      { "cell": "E2", "formula": "=D2*0.1" },
      { "cell": "E3", "formula": "=D3*0.1" },
      { "cell": "E4", "formula": "=D4*0.1" },
      { "cell": "F2", "formula": "=D2+E2" },
      { "cell": "F3", "formula": "=D3+E3" },
      { "cell": "F4", "formula": "=D4+E4" },
      { "cell": "D5", "formula": "=SUM(D2:D4)" },
      { "cell": "E5", "formula": "=SUM(E2:E4)" },
      { "cell": "F5", "formula": "=SUM(F2:F4)" }
    ]
  }
}
```

### Sintassi formula mista
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data",
    "formulas": [
      { "cell": "F4", "formula": "=D4*2" },
      { "cell": "F5", "formula": "D5*2" },
      { "cell": "F6", "formula": "=D6*2" },
      { "cell": "G4", "formula": "=D4+10" },
      { "cell": "G5", "formula": "=D5+10" },
      { "cell": "G6", "formula": "=D6+10" },
      { "cell": "G7", "formula": "=SUM(G4:G6)" }
    ]
  }
}
```

## Funzioni Excel comuni

### Funzioni matematiche
- `SUM(range)` - Somma valori nell'intervallo
- `AVERAGE(range)` - Calcola la media
- `MIN(intervallo)` - Trova il valore minimo
- `MAX(intervallo)` - Trova il valore massimo
- `COUNT(intervallo)` - Conta le celle numeriche

### Funzioni logiche
- `IF(condizione, valore_vero, valore_falso)` - Logica condizionale
- `AND(condizione1, condizione2)` - E logico
- `OR(condizione1, condizione2)` - O logico

### Funzioni di testo
- `CONCATENATE(testo1, testo2)` - Unisci testo
- `LEFT(testo, num_caratteri)` - Estrai caratteri a sinistra
- `RIGHT(testo, num_caratteri)` - Estrai caratteri a destra
- `LEN(testo)` - Lunghezza del testo

## Pratiche consigliate

1. **Sintassi della formula**: Sia `=SUM(A1:A10)` che `SUM(A1:A10)` funzionano
2. **Riferimenti di cella**: Usa riferimenti assoluti (`$A$1`) quando necessario
3. **Gestione degli errori**: Prova le formule con dati semplici prima
4. **Operazioni batch**: Usa operazioni di gruppo per più formule simili
5. **Validazione delle formule**: Verifica i risultati dopo aver applicato le formule

## Gestione degli errori

### Array di formule vuote
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "formulas": []
  }
}
```
**Risultato**: Errore di convalida per array vuoto

### Formula non valida
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "cell": "A1",
    "formula": "=INVALID_FUNCTION(A1)"
  }
}
```
**Risultato**: Errore di sintassi della formula
{{< app/cells/assistant language="nodejs-cpp" >}}

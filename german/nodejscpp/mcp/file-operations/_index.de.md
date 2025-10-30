---
title: Excel Datei und Datenoperationen
linktitle: Datei und Datenoperationen
type: docs
weight: 10
url: /de/nodejs-cpp/mcp/file-operations
keywords: "Excel Dateioperationen, Excel Datenoperationen, Excel Arbeitsmappe erstellen, Excel Tabellenblatt, Excel Daten lesen, Excel Daten schreiben"
description: "Excel Datei und Datenoperationen  Arbeitsmappen erstellen, Tabellenblätter verwalten, Excel Daten mit KI Automatisierung lesen und schreiben"
---

# Excel-Datei- und Datenoperationen

Verwalten Sie **Excel-Dateien** und **Datenoperationen** mit KI-gesteuerter Automatisierung. Erstellen Sie **Excel-Arbeitsmappen**, verwalten Sie **Tabellenblätter** und führen Sie **Excel-Daten** Lese-/Schreiboperationen durch.

## Verfügbare Tools

- `create_workbook` - Neue **Excel-Arbeitsmappen** mit **KI Excel** Automatisierung erstellen
- `create_worksheet` - **Excel-Tabellenblätter** zu bestehenden **Excel-Arbeitsmappen** hinzufügen
- `get_workbook_info` - Metadaten und Informationen von **Excel-Arbeitsmappen** abrufen
- `read_data_from_excel` - Daten aus **Excel-Tabellenblättern** mit **KI-gestützter** Präzision lesen
- `write_data_to_excel` - Daten in **Excel-Tabellenblätter** über **Excel MCP** schreiben

## Excel-Arbeitsmappen erstellen

### Einfache Arbeitsmappe erstellen
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### Arbeitsmappe mit benutzerdefiniertem Blatt erstellen
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## Tabellenblätter verwalten

### Neues Tabellenblatt hinzufügen
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### Arbeitsmappe-Informationen abrufen
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Excel-Daten schreiben

### Überschriften und Daten schreiben
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

### Daten an benutzerdefinierte Position schreiben
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

## Excel-Daten lesen

### Voll genutzten Bereich lesen
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### Bestimmten Bereich lesen
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

### Vom Standardort lesen
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

## Komplettes Arbeitsablaufbeispiel

### 1. Erstellen Sie Ihren ersten Excel-Bericht
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. Zusammenfassungsblatt hinzufügen
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. Verkaufsdaten schreiben
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

### 4. Daten überprüfen
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

### 5. Arbeitsmappendestruktur prüfen
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## Best Practices

1. **Dateipfade**: Verwenden Sie relative Pfade für bessere Portabilität
2. **Blattnamen**: Verwenden Sie beschreibende Namen für Arbeitsblätter
3. **Datenstruktur**: Organisieren Sie Daten mit klaren Überschriften
4. **Bereich lesen**: Geben Sie Bereiche für große Datensätze an
5. **Fehlerbehandlung**: Überprüfen Sie die Dateiexistenz vor Operationen

## Häufige Muster

### Datenimportmuster
1. Arbeitsmappe erstellen
2. Rohdaten eingeben
3. Zur Überprüfung erneut lesen
4. Mit Formeln verarbeiten

### Mehrblattberichte
1. Arbeitsmappe mit Hauptblatt erstellen
2. Zusammenfassungs-/Analysegertblätter hinzufügen
3. Daten in jedes Blatt schreiben
4. Blätter mit Formeln verknüpfen

### Datenvalidierung
1. Daten schreiben
2. Bestimmte Bereiche erneut lesen
3. Datenintegrität überprüfen
4. Fehlende Werte behandeln 
{{< app/cells/assistant language="nodejs-cpp" >}}

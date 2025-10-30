---
title: Excel Zeilen und Spaltoperationen
linktitle: Zeilen und Spaltoperationen
type: docs
weight: 50
url: /de/nodejs-cpp/mcp/row-column-operations
keywords: "Excel Zeilenoperationen, Excel Spaltenoperationen, Excel Layout Management, Zeilen einfügen, Spalten löschen, Excel Zellen anpassen"
description: "Excel Zeilen und Spaltenoperationen  Einfügen, Löschen, Anpassen, Ausblenden/anzeigen von Zeilen und Spalten mit KI Automatisierung"
---

# Excel Zeilen- und Spaltenoperationen

Verwalten Sie **Excel Zeilen- und Spaltenoperationen** mit KI-gestützter Automatisierung. Fügen Sie **Excel Zeilen** und **Spalten** ein, löschen, passen an, blenden aus/ein, um eine perfekte Tabellenlayoutverwaltung zu gewährleisten.

## Verfügbare Tools

- `row_column_operations` - **Excel Zeilen/Spalten Operationen** (einfügen, löschen, anpassen, ausblenden/einblenden) mit **KI Excel**
- `row_column_operations_batch` - Mehrere **Excel Zeilen/Spalten Operationen** in Batch mit **Excel MCP** durchführen

## Einzelne Operationen

### Zeilen Einfügen
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

### Spalten Löschen
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

### Zeilenhöhe festlegen
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

### Spaltenbreite festlegen
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

## Stapeloperationen

### Umfassende Layout-Einrichtung
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

### Einfüge- und Löschoperationen
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

### Verstecken- und Anzeigen-Operationen
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

### Automatisches Anpassen der Operationen
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

## Referenz für Operationstypen

### Einfügeoperationen
- `insert_rows` - Neue Zeilen an der angegebenen Position einfügen
- `insert_columns` - Neue Spalten an der angegebenen Position einfügen

### Löschoperationen  
- `delete_rows` - Angegebene Zeilen löschen
- `delete_columns` - Angegebene Spalten löschen

### Größenänderungsoperationen
- `set_row_height` - Spezifische Zeilenhöhe in Punkten festlegen
- `set_column_width` - Spezifische Spaltenbreite in Zeichen festlegen
- `auto_fit_rows` - Zeilen automatisch an Inhaltshöhe anpassen
- `auto_fit_columns` - Spalten automatisch an Inhaltsbreite anpassen

### Sichtbarkeitsoperationen
- `hide_rows` - Angegebene Zeilen ausblenden
- `unhide_rows` - Versteckte Zeilen anzeigen
- `hide_columns` - Angegebene Spalten ausblenden
- `unhide_columns` - Versteckte Spalten anzeigen

## Bereichsspezifikationen

### Zeilenbereiche
- `"1"` - Einzelne Zeile (Zeile 1)
- `"1:3"` - Bereich von Zeilen (Zeilen 1 bis 3)
- `"5:10"` - Mehrere aufeinanderfolgende Zeilen

### Spaltenbereiche
- `"A"` - Einzelne Spalte (Spalte A)
- `"A:C"` - Bereich von Spalten (Spalten A bis C)
- `"D:F"` - Mehrere aufeinanderfolgende Spalten

## Erweiterte Beispiele

### Berichtskopf einrichten
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

### Layout der Datentabelle
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

### Präsentationslayout
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

## Messrichtlinien

### Zeilenhöhen (Punkte)
- `15` - Standardzeilenhöhe
- `20` - Leicht erhöht für bessere Lesbarkeit
- `25` - Gut für Überschriften
- `30` - Große Überschriften
- `40` - Extra groß für Titel

### Spaltenbreiten (Zeichen)
- `8` - Schmale Spalten (Daten, Codes)
- `12` - Standard-Datenspalten
- `15` - Mittlere Textspalten
- `20` - Breite Textspalten
- `25` - Extra breite für Beschreibungen
- `30` - Sehr breit für langen Text

## Best Practices

1. **Header-Größe**: Überschriften höher und breiter machen für Akzentuierung
2. **Datenkonsistenz**: Konsistente Zeilenhöhen für Datenzeilen verwenden
3. **Automatische Anpassung**: Auto-Fit für dynamische Inhaltsgrößen verwenden
4. **Verstecken ungenutzter**: Leere Zeilen/Spalten für eine sauberere Optik ausblenden
5. **Logische Gruppierung**: Zusammengehörende Änderungsoperationen in Chargen gruppieren

## Häufige Muster

### Berichtaufbau-Muster
1. Titelfelder oben einfügen
2. Zeilenhöhe der Header-Zeile einstellen
3. Automatisches Anpassen der Daten spalten
4. Festlegung der Standard-Daten Zeilenhöhe
5. Unsichtbare Bereiche ausblenden

### Datenimportmuster
1. Zeilen für neue Daten einfügen
2. Spalten automatisch an Inhalt anpassen
3. Zeilenhöhen standardisieren
4. Berechnungsspalten ausblenden

### Präsentationsmuster
1. Detailzeilen/-spalten ausblenden
2. Zusammenfassungsbereiche vergrößern
3. Präsentationsfreundliche Abmessungen festlegen
4. Nur relevante Daten anzeigen

## Fehlerbehandlung

### Ungültiger Zeilenbereich
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
**Ergebnis**: Fehler - Zeilennummern beginnen bei 1

### Ungültiger Spaltenbereich
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
**Ergebnis**: Kann erfolgreich sein, aber außerhalb des üblichen Gebrauchs

### Fehlende erforderliche Parameter
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
**Ergebnis**: Fehler - Höhenparameter erforderlich 
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Wie man ein PivotChart mit Golang über C++ hinzufügt
linktitle: Pivot Diagramm
type: docs
weight: 100
url: /de/go-cpp/how-to-add-pivot-chart/
description: Wie man mit Aspose.Cells unter Verwendung von Golang über C++ ein PivotChart hinzufügt.
keywords: PivotChart
---

## Was ist ein PivotChart

Ein Pivot-Chart ist eine visuelle Darstellung der Daten in einer Pivot-Tabelle. Pivot-Charts bieten eine Möglichkeit, Zusammenfassungen zu erstellen, zu analysieren, zu erkunden und präsentabel zu machen. Hier sind einige wichtige Funktionen und Aspekte von Pivot-Charts:

1. **Dynamische Datenanzeige**: Pivot-Diagramme aktualisieren sich automatisch, um Änderungen in der Pivot-Tabelle widerzuspiegeln. Wenn Sie Felder in der Pivot-Tabelle hinzufügen oder entfernen, wird das Pivot-Diagramm entsprechend aktualisiert.

1. **Interaktiv**: Pivot-Diagramme sind interaktiv, Nutzer können filtern, sortieren und in die Daten hineinzoomen. Das erleichtert die Erkundung verschiedener Aspekte des Datensatzes.

1. **Flexibles Layout**: Nutzer können das Layout des Pivot-Diagramms durch Drag & Drop von Feldern ändern, was Flexibilität bei der Visualisierung der Daten bietet.

1. **Verschiedene Diagrammtypen**: Pivot-Diagramme können mit verschiedenen Diagrammtypen wie Balkendiagrammen, Liniendiagrammen, Tortendiagrammen und mehr erstellt werden, abhängig von der Natur der Daten und den Erkenntnissen, die Sie gewinnen möchten.

1. **Zusammenfassung**: Pivot-Diagramme fassen große Datenmengen zusammen und können Summen, Durchschnitte, Zählungen oder andere Zusammenfassungsstatistiken anzeigen.

1. **Filterung**: Sie bieten Filtermöglichkeiten, mit denen Sie nur die Daten anzeigen können, die bestimmte Kriterien erfüllen.

<br>
Pivot-Diagramme werden häufig in Business Intelligence und Datenanalyse verwendet, um eine klare und prägnante visuelle Zusammenfassung komplexer Datensätze zu bieten. Sie sind ein mächtiges Werkzeug, um datengetriebene Entscheidungen zu treffen.

## So fügen Sie ein PivotChart mit Aspose.Cells hinzu

### **Hinzufügen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen:

1. Fügen Sie einige Daten in Tabellenzellen ein, indem Sie die Methode `PutValue` oder `SetValue` eines `Cell`-Objekts verwenden. Sie können auch eine bereits mit Daten gefüllte Vorlagendatei verwenden. Die Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
1. Fügen Sie eine Pivot-Tabelle zum Arbeitsblatt hinzu, indem Sie die Methode `Add` der `PivotTables`-Sammlung aufrufen (eingeschlossen im `Worksheet`-Objekt).
1. Greifen Sie auf das neue `PivotTable`-Objekt aus der `PivotTables`-Sammlung durch Angabe seines Index zu. Verwenden Sie eines der Pivot-Tabellen-Objekte, die im `PivotTable`-Objekt eingeschlossen sind, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}
### **Hinzufügen eines Pivot-Diagramms**

Um ein PivotChart mit Aspose.Cells zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie die `PivotSource` des Diagramms so, dass sie sich auf eine vorhandene Pivot-Tabelle im Spreadsheet bezieht.
1. Setzen Sie andere Attribute.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}

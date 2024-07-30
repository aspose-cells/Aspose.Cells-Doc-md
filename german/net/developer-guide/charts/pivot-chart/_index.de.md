---
title: Wie man ein PivotChart mit Aspose.Cells hinzufügt
linktitle: Pivot Diagramm
type: docs
weight: 100
url: /de/net/how-to-add-pivot-chart/
description: Wie man ein PivotChart mit Aspose.Cells hinzufügt.
keywords: PivotChart
---
## Was ist ein PivotChart

Ein Pivot-Diagramm ist eine visuelle Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme bieten eine Möglichkeit, Zusammenfassungen zu analysieren, zu erkunden und zu präsentieren. Hier sind einige wichtige Funktionen und Aspekte von Pivot-Diagrammen:

1. Dynamische Datenwiedergabe: Pivot-Diagramme aktualisieren sich automatisch bei Änderungen in der Pivot-Tabelle. Wenn Sie Felder hinzufügen oder entfernen, aktualisiert sich das Pivot-Diagramm entsprechend.

1. Interaktiv: Pivot-Diagramme sind interaktiv und ermöglichen es den Benutzern, Daten zu filtern, zu sortieren und in die Daten einzutauchen. Dies erleichtert die Erkundung verschiedener Aspekte des Datensatzes.

1. Flexible Layout: Benutzer können das Layout des Pivot-Diagramms ändern, indem sie Felder ziehen und ablegen, was Flexibilität in der Visualisierung der Daten bietet.

1. Verschiedene Diagrammtypen: Pivot-Diagramme können mit verschiedenen Diagrammtypen wie Balkendiagrammen, Liniendiagrammen, Kreisdiagrammen und mehr erstellt werden, abhängig von der Art der Daten und den Einblicken, die Sie gewinnen möchten.

1. Zusammenfassung: Pivot-Diagramme fassen große Datenmengen zusammen und können Summen, Durchschnitte, Zählungen oder andere Zusammenfassungsstatistiken anzeigen.

1. Filterung: Sie bieten Filtermöglichkeiten, mit denen Sie nur die Daten anzeigen können, die bestimmte Kriterien erfüllen.

<br>
Pivot-Diagramme werden häufig in der Business Intelligence und Datenanalyse eingesetzt, um eine klare und prägnante visuelle Zusammenfassung komplexer Datensätze zu bieten. Sie sind ein leistungsstolles Werkzeug für datenbasierte Entscheidungen.

## So fügen Sie ein PivotChart mit Aspose.Cells hinzu

### **Hinzufügen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen:

1. Fügen Sie einige Daten in Zellen eines Arbeitsblatts mit der PutValue/setValue-Methode eines Cell-Objekts ein. Sie können auch eine Vorlagendatei verwenden, die bereits mit Daten gefüllt ist. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode add der PivotTables-Sammlung aufrufen (die im Arbeitsblatt-Objekt gekapselt ist).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Sammlung zu, indem Sie seinen Index übergeben. # Verwenden Sie eines der in dem PivotTable-Objekt gekapselten Pivot-Tabellenobjekte, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Hinzufügen eines Pivot-Diagramms**

Um ein PivotChart mit Aspose.Cells zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie den PivotSource des Diagramms so, dass er auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Setzen Sie andere Attribute.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}


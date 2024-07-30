---
title: Wie man ein PivotChart mit Aspose.Cells hinzufügt
linktitle: Pivot Diagramm
type: docs
weight: 100
url: /de/java/how-to-add-pivot-chart/
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
### **Erstellen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen:

1. Fügen Sie einige Daten in Zellen eines Arbeitsblatts mit der PutValue/setValue-Methode eines Cell-Objekts ein. Sie können auch eine Vorlagendatei verwenden, die bereits mit Daten gefüllt ist. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode add der PivotTables-Sammlung aufrufen (die im Arbeitsblatt-Objekt gekapselt ist).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Sammlung zu, indem Sie seinen Index übergeben.
1. Verwenden Sie eines der im PivotTable-Objekt gekapselten Pivot-Table-Objekte, um das Table zu verwalten.

Ein Codebeispiel wird unten gegeben. Wenn der Code ausgeführt wird, wird eine neue Datei generiert: pivotTable_test.xls.

**Eingangsdaten** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Das Output-Pivot-Table**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Erstellen eines Pivot-Diagramms basierend auf dem Pivot-Table**

Um ein Pivot-Diagramm mit Aspose.Cells zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie den PivotSource des Diagramms so, dass er auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Setzen Sie andere Attribute.

Unten ist der Code, den das Bauteil verwendet, um die Aufgabe zu erfüllen. Wenn der Code ausgeführt wird, wird eine neue Datei generiert: pivotChart_test.xls.

**Das Pivot-Diagrammblatt**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie man Pivot-Tabellen und Pivot-Diagramme mit Aspose.Cells erstellt. Hoffentlich wird es Ihnen helfen, diese Funktionen in Ihren eigenen Szenarien zu verwenden.

Aspose.Cells hat jahrelange Forschung, Design und sorgfältige Abstimmung genossen.

Wir begrüßen Ihre Anfragen, Kommentare und Vorschläge im [Aspose.Cells-Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine schnelle Antwort.

{{% /alert %}}

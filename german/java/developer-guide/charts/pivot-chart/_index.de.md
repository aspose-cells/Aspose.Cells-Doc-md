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
Ein Pivot-Chart ist eine visuelle Darstellung der Daten in einer Pivot-Tabelle. Pivot-Charts bieten eine Möglichkeit, Zusammenfassungen zu erstellen, zu analysieren, zu erkunden und präsentabel zu machen. Hier sind einige wichtige Funktionen und Aspekte von Pivot-Charts:

1. Dynamische Datenrepräsentation: Pivot-Charts aktualisieren sich automatisch, um Änderungen an der Pivot-Tabelle widerzuspiegeln. Wenn Felder in der Pivot-Tabelle hinzugefügt oder entfernt werden, wird das Pivot-Chart entsprechend aktualisiert.

1. Interaktiv: Pivot-Charts sind interaktiv, ermöglichen es Benutzern, Daten zu filtern, zu sortieren und zu vertiefen. Dadurch ist es einfach, verschiedene Aspekte des Datensatzes zu erkunden.

1. Flexibles Layout: Benutzer können das Layout des Pivot-Diagrams durch Ziehen und Ablegen von Feldern ändern, was Flexibilität bei der Visualisierung von Daten bietet.

1. Verschiedene Diagrammtypen: Pivot-Diagramme können mit verschiedenen Diagrammtypen wie Säulendiagrammen, Liniendiagrammen, Kreisdiagrammen und mehr erstellt werden, je nach Art der Daten und den gewünschten Erkenntnissen.

1. Zusammenfassung: Pivot-Diagramme fassen große Datenmengen zusammen und können Summen, Durchschnitte, Zählen oder andere Zusammenfassungsstatistiken anzeigen.

1. Filtern: Sie bieten Filterfunktionen, mit denen nur Daten angezeigt werden, die bestimmte Kriterien erfüllen.

<br>
Pivot-Diagramme werden häufig in Business Intelligence und Datenanalyse verwendet, um eine klare und prägnante visuelle Zusammenfassung komplexer Datensätze zu bieten. Sie sind ein mächtiges Werkzeug, um datengetriebene Entscheidungen zu treffen.

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
{{< app/cells/assistant language="java" >}}

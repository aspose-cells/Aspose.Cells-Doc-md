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

Ein PivotChart in Excel ist eine grafische Darstellung von Daten, die aus einer PivotTable erstellt wird. Es ermöglicht Benutzern, Daten dynamisch zu visualisieren und zu analysieren, indem Informationen in Diagrammform zusammengefasst und angezeigt werden. PivotCharts sind interaktiv und können leicht modifiziert werden, um verschiedene Perspektiven der Daten zu zeigen, was es zu einem leistungsstarken Werkzeug für die Datenanalyse und Präsentation in Excel macht.

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

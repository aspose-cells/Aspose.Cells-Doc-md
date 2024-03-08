---
title: So fügen Sie ein PivotChart mit Aspose.Cells hinzu
linktitle: Pivot-Diagramm
type: docs
weight: 100
url: /de/java/how-to-add-pivot-chart/
description: So fügen Sie ein PivotChart mit Aspose.Cells hinzu.
keywords: PivotChart
---
##  Was ist PivotChart?

Ein PivotChart in Excel ist eine grafische Darstellung von Daten, die aus einer PivotTable erstellt wurden. Es ermöglicht Benutzern die dynamische Visualisierung und Analyse von Daten, indem Informationen in Diagrammform zusammengefasst und angezeigt werden. PivotCharts sind interaktiv und können leicht geändert werden, um verschiedene Perspektiven der Daten anzuzeigen, was sie zu einem leistungsstarken Werkzeug für die Datenanalyse und Präsentation in Excel macht.

##  So fügen Sie ein PivotChart mit Aspose.Cells hinzu
###  **Erstellen einer Pivot-Tabelle**

So erstellen Sie eine Pivot-Tabelle mit Aspose.Cells:

1. Fügen Sie mithilfe der PutValue/setValue-Methode eines Cell-Objekts einige Daten zu den Zellen eines Arbeitsblatts hinzu. Sie verwenden auch eine bereits mit Daten gefüllte Vorlagendatei. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Add-Methode der PivotTables-Sammlung aufrufen (gekapselt im Worksheet-Objekt).
1. Greifen Sie über die PivotTables-Auflistung auf das neue PivotTable-Objekt zu, indem Sie dessen Index übergeben.
1. Verwenden Sie zum Verwalten der Tabelle eines der im PivotTable-Objekt gekapselten Pivot-Tabellenobjekte.

Nachfolgend finden Sie ein Codebeispiel. Durch die Ausführung des Codes wird eine neue Datei generiert: PivotTable_test.xls.

**Eingabedaten** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Die Ausgabe-Pivot-Tabelle**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **Erstellen eines Pivot-Diagramms basierend auf der Pivot-Tabelle**

So erstellen Sie ein Pivot-Diagramm mit Aspose.Cells:

1. Fügen Sie ein Diagramm hinzu.
1. Legen Sie die PivotSource des Diagramms so fest, dass sie auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Legen Sie andere Attribute fest.

Nachfolgend finden Sie den Code, den die Komponente zum Ausführen der Aufgabe verwendet. Durch die Ausführung des Codes wird eine neue Datei generiert: PivotChart_test.xls.

**Das Pivot-Diagrammblatt**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie Sie Pivot-Tabellen und Pivot-Diagramme mit Aspose.Cells erstellen. Wir hoffen, dass er Ihnen dabei hilft, diese Funktionen in Ihren eigenen Szenarien zu nutzen.

Aspose.Cells hat von jahrelanger Forschung, Design und sorgfältiger Abstimmung profitiert.

 Wir freuen uns über Ihre Fragen, Kommentare und Vorschläge unter[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine zeitnahe Antwort.

{{% /alert %}}

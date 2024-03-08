---
title: So fügen Sie ein PivotChart mit Aspose.Cells hinzu
linktitle: Pivot-Diagramm
type: docs
weight: 100
url: /de/net/how-to-add-pivot-chart/
description: So fügen Sie ein PivotChart mit Aspose.Cells hinzu.
keywords: PivotChart
---
##  Was ist PivotChart?

Ein PivotChart in Excel ist eine grafische Darstellung von Daten, die aus einer PivotTable erstellt wurden. Es ermöglicht Benutzern die dynamische Visualisierung und Analyse von Daten, indem Informationen in Diagrammform zusammengefasst und angezeigt werden. PivotCharts sind interaktiv und können leicht geändert werden, um verschiedene Perspektiven der Daten anzuzeigen, was sie zu einem leistungsstarken Werkzeug für die Datenanalyse und Präsentation in Excel macht.

##  So fügen Sie ein PivotChart mit Aspose.Cells hinzu

###  **Hinzufügen einer Pivot-Tabelle**

So erstellen Sie eine Pivot-Tabelle mit Aspose.Cells:

1. Fügen Sie mithilfe der PutValue/setValue-Methode eines Cell-Objekts einige Daten zu den Zellen eines Arbeitsblatts hinzu. Sie verwenden auch eine bereits mit Daten gefüllte Vorlagendatei. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Add-Methode der PivotTables-Sammlung aufrufen (gekapselt im Worksheet-Objekt).
1. Greifen Sie über die PivotTables-Auflistung auf das neue PivotTable-Objekt zu, indem Sie dessen Index übergeben. # Verwenden Sie eines der im PivotTable-Objekt gekapselten Pivot-Tabellenobjekte, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **Hinzufügen eines Pivot-Diagramms**

So erstellen Sie ein PivotChart mit Aspose.Cells:

1. Fügen Sie ein Diagramm hinzu.
1. Legen Sie die PivotSource des Diagramms so fest, dass sie auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Legen Sie andere Attribute fest.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}


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

Ein PivotChart in Excel ist eine grafische Darstellung von Daten, die aus einer PivotTable erstellt wird. Es ermöglicht Benutzern, Daten dynamisch zu visualisieren und zu analysieren, indem Informationen in Diagrammform zusammengefasst und angezeigt werden. PivotCharts sind interaktiv und können leicht modifiziert werden, um verschiedene Perspektiven der Daten zu zeigen, was es zu einem leistungsstarken Werkzeug für die Datenanalyse und Präsentation in Excel macht.

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


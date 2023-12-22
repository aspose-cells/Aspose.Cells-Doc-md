---
title: Aktualisieren und berechnen Sie die Pivot-Tabelle mit berechneten Elementen
type: docs
weight: 40
url: /de/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: In diesem Artikel wird gezeigt, wie Sie eine Pivot-Tabelle mit berechneten Elementen mit Aspose.Cells for Python via .NET aktualisieren und berechnen.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET unterstützt jetzt das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Bitte nutzen Sie die[**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) Und[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) wie gewohnt, um diese Funktion auszuführen.

{{% /alert %}}

##  **Aktualisieren und berechnen Sie die Pivot-Tabelle mit berechneten Elementen**

 Der folgende Beispielcode lädt die[Quell-Excel-Datei](5115238.xlsx)die eine Pivot-Tabelle mit drei berechneten Elementen wie „add“, „div“, „div2“ enthält. Wir ändern zunächst den Wert der Zelle D2 auf 20, aktualisieren und berechnen dann die Pivot-Tabelle mithilfe der APIs Aspose.Cells, for Python und via .NET und speichern die Arbeitsmappe im Format PDF. Die Ergebnisse im[Ausgabe PDF](5115229.pdf) zeigt, dass Aspose.Cells for Python via .NET die Pivot-Tabelle aktualisiert und berechnet hat, nachdem die Elemente erfolgreich berechnet wurden. Sie können dies mit Microsoft Excel überprüfen, indem Sie manuell den Wert 20 in Zelle D2 eingeben und dann die Pivot-Tabelle über die Tastenkombination Alt+F5 aktualisieren oder auf die Schaltfläche „Aktualisieren“ der Pivot-Tabelle klicken.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}

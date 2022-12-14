---
title: Pivot-Tabelle mit berechneten Elementen aktualisieren und berechnen
type: docs
weight: 40
url: /de/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells unterstützt jetzt das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Bitte verwenden Sie die[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) und[**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) wie gewohnt, um diese Funktion auszuführen.

{{% /alert %}}

## **Pivot-Tabelle mit berechneten Elementen aktualisieren und berechnen**

 Der folgende Beispielcode lädt die[Excel-Quelldatei](5115238.xlsx)die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Wir ändern zuerst den Wert von Zelle D2 in 20 und aktualisieren und berechnen dann die Pivot-Tabelle mit Aspose.Cells-APIs und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse in der[PDF ausgeben](5115229.pdf) zeigt, dass Aspose.Cells die Pivot-Tabelle aktualisiert und berechnet hat, nachdem Elemente erfolgreich berechnet wurden. Sie können es mit Microsoft Excel überprüfen, indem Sie manuell den Wert 20 in Zelle D2 eingeben und dann die Pivot-Tabelle über die Tastenkombination Alt+F5 aktualisieren oder auf die Schaltfläche Aktualisieren der Pivot-Tabelle klicken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}

---
title: Pivot Tabelle aktualisieren und Berechnen von Pivot Tabellen mit berechneten Elementen
type: docs
weight: 40
url: /de/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt jetzt das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Verwenden Sie bitte [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) und [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) wie gewohnt, um diese Funktion auszuführen.

{{% /alert %}}

## **Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen**

Der folgende Beispielscode lädt die [Quellexceldatei](5115238.xlsx), die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Wir ändern zuerst den Wert der Zelle D2 auf 20 und aktualisieren und berechnen dann die Pivot-Tabelle mithilfe der Aspose.Cells-APIs und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse im [Ausgabe-PDF](5115229.pdf) zeigen, dass Aspose.Cells die Pivot-Tabelle mit berechneten Elementen erfolgreich aktualisiert und berechnet hat. Sie können dies mit Microsoft Excel überprüfen, indem Sie den Wert 20 manuell in Zelle D2 eingeben und dann die Pivot-Tabelle über die Tastenkombination Alt+F5 oder durch Klicken auf die Schaltfläche zum Aktualisieren der Pivot-Tabelle aktualisieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}

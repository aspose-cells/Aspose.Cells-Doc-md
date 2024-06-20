---
title: Pivot Tabelle aktualisieren und Berechnen von Pivot Tabellen mit berechneten Elementen
type: docs
weight: 130
url: /de/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt nun das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Verwenden Sie bitte [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) und [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) wie gewohnt, um diese Funktion auszuführen.

{{% /alert %}}

## **Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen**

Der folgende Beispielcode lädt die [Quelldatei der Excel-Datei](5473428.xlsx), die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Wir ändern zuerst den Wert der Zelle D2 auf 20 und aktualisieren und berechnen dann die Pivot-Tabelle mit den Aspose.Cells APIs und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse in der [Ausgabedatei im PDF-Format](5473431.pdf) zeigen, dass Aspose.Cells erfolgreich die Pivot-Tabelle mit berechneten Elementen aktualisiert und berechnet hat. Sie können dies in Microsoft Excel überprüfen, indem Sie den Wert 20 manuell in die Zelle D2 eingeben und dann die Pivot-Tabelle über die Tastenkombination Alt+F5 oder durch Klicken auf die Schaltfläche Pivot-Tabelle aktualisieren aktualisieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}

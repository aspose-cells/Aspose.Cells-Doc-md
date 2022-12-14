---
title: Pivot-Tabelle mit berechneten Elementen aktualisieren und berechnen
type: docs
weight: 130
url: /de/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells unterstützt jetzt das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Bitte verwende[**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) und[**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) wie gewohnt, um diese Funktion auszuführen.

{{% /alert %}}

## **Pivot-Tabelle mit berechneten Elementen aktualisieren und berechnen**

 Der folgende Beispielcode lädt die[Excel-Quelldatei](5473428.xlsx)die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Wir ändern zuerst den Wert von Zelle D2 in 20 und aktualisieren und berechnen dann die Pivot-Tabelle mit Aspose.Cells-APIs und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse in der[PDF ausgeben](5473431.pdf) zeigt, dass Aspose.Cells die Pivot-Tabelle aktualisiert und berechnet hat, nachdem Elemente erfolgreich berechnet wurden. Sie können es mit Microsoft Excel überprüfen, indem Sie manuell den Wert 20 in Zelle D2 eingeben und dann die Pivot-Tabelle über die Tastenkombination Alt+F5 aktualisieren oder auf die Schaltfläche Aktualisieren der Pivot-Tabelle klicken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}

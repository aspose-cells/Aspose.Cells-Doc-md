---
title: Aktualisieren und Berechnen einer Pivot Tabelle mit Berechneten Elementen in Golang über C++
linktitle: Pivot Tabelle aktualisieren und Berechnen von Pivot Tabellen mit berechneten Elementen
type: docs
weight: 40
url: /de/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aktualisieren und Berechnen einer Pivot Tabelle mit berechneten Elementen unter Verwendung von Aspose.Cells in Golang über C++
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt jetzt das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Verwenden Sie bitte [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) und [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) wie gewohnt, um diese Funktion auszuführen.

{{% /alert %}}

## **Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen**

Das folgende Beispiel lädt die [Quell-Excel-Datei](5115238.xlsx), die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Zuerst ändern wir den Wert der Zelle D2 auf 20 und aktualisieren sowie berechnen anschließend die Pivot-Tabelle mit den APIs von Aspose.Cells und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse im [Ausgabe-PDF](5115229.pdf) zeigen, dass Aspose.Cells die Pivot-Tabelle mit den berechneten Elementen erfolgreich aktualisiert und berechnet hat. Sie können dies überprüfen, indem Sie in Microsoft Excel manuell den Wert 20 in die Zelle D2 eingeben und dann die Pivot-Tabelle mit der Tastenkombination Alt+F5 aktualisieren oder die Schaltfläche "PivotTable aktualisieren" klicken.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}

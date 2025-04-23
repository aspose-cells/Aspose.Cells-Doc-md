---
title: Pivot Tabelle aktualisieren und Berechnen von Pivot Tabellen mit berechneten Elementen
type: docs
weight: 40
url: /de/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ unterstützt jetzt das Aktualisieren und Berechnen eines Pivot-Table mit berechneten Elementen. Bitte verwenden Sie wie üblich [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) und [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--), um diese Funktion durchzuführen.

{{% /alert %}}

## **Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen**

Der folgende Beispielcode lädt die [Quelldatei](5115238.xlsx), die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Wir ändern zuerst den Wert der Zelle D2 auf 20 und aktualisieren und berechnen dann die Pivot-Tabelle mit den APIs von Aspose.Cells for Node.js via C++ und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse im [Ausgabe-PDF](5115229.pdf) zeigen, dass Aspose.Cells for Node.js via C++ die Pivot-Tabelle mit den berechneten Elementen erfolgreich aktualisiert und berechnet hat. Sie können dies auch manuell in Microsoft Excel prüfen, indem Sie den Wert 20 in Zelle D2 eingeben und die Aktualisierung der Pivot-Tabelle mit der Tastenkombination Alt+F5 oder durch Klicken auf die Pivot-Tabelle-Aktualisieren-Schaltfläche durchführen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}


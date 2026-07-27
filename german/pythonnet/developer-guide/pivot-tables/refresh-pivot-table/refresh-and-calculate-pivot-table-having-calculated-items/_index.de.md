---
title: Pivot Tabelle aktualisieren und Berechnen von Pivot Tabellen mit berechneten Elementen
type: docs
weight: 40
url: /de/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Dieser Artikel zeigt, wie Sie Pivot Tabellen mit berechneten Elementen aktualisieren und berechnen können, mit Aspose.Cells für Python via .NET.
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Aktualisieren und Berechnen von Pivot Tabellen mit berechneten Elementen
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET unterstützt jetzt das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Verwenden Sie wie gewohnt [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) und [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#), um diese Funktion auszuführen.

{{% /alert %}}

## **Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen**

Der folgende Beispielcode lädt die [Quelldatei für Excel](5115238.xlsx), die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Zuerst ändern wir den Wert der Zelle D2 auf 20 und aktualisieren und berechnen dann die Pivot-Tabelle mithilfe der Aspose.Cells für Python via .NET-APIs und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse im [Ausgabe-PDF](5115229.pdf) zeigen, dass Aspose.Cells für Python via .NET erfolgreich die Pivot-Tabelle mit berechneten Elementen aktualisiert und berechnet hat. Sie können dies überprüfen, indem Sie den Wert 20 manuell in Zelle D2 eingeben und dann die Pivot-Tabelle über die Tastenkombination Alt+F5 oder Klicken auf die Pivot-Tabelle aktualisieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

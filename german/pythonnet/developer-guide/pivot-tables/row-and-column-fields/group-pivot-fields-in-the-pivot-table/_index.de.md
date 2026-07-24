---
title: Gruppieren von Pivot Feldern in der Pivot Tabelle
type: docs
weight: 80
url: /de/python-net/group-pivot-fields-in-the-pivot-table/
description: Wie man Pivot Felder in der Pivot Tabelle mit Aspose.Cells für Python via .NET gruppiert.
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Wie man Pivot Felder in der Pivot Tabelle mit Aspose.Cells für Python Excel Bibliothek gruppiert.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht es Ihnen, Pivot-Felder der Pivot-Tabelle zu gruppieren. Wenn eine große Menge an Daten mit einem Pivot-Feld verbunden ist, ist es oft nützlich, sie in Abschnitte zu gruppieren. Aspose.Cells für Python via .NET bietet diese Funktion ebenfalls über die [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)-Methode.

## **Wie man Pivot-Felder in der Pivot-Tabelle gruppiert**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716818.xlsx) und führt eine Gruppierung des ersten Pivot-Felds mit der Methode [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float) durch. Anschließend aktualisiert und berechnet er die Daten der Pivot-Tabelle und speichert die Arbeitsmappe als [Ausgabedatei Excel](64716817.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispieldatei Excel. Wie im Screenshot zu sehen ist, ist das erste Pivot-Feld nun nach Monaten und Quartalen gruppiert.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
{{< app/cells/assistant language="python-net" >}}

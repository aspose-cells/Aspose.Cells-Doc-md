---
title: Gruppieren von Pivot Feldern in der Pivot Tabelle
type: docs
weight: 80
url: /de/net/group-pivot-fields-in-the-pivot-table/
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht es Ihnen, Pivot-Felder der Pivot-Tabelle zu gruppieren. Wenn eine große Menge von Daten mit einem Pivot-Feld verbunden ist, ist es oft nützlich, sie in Abschnitte zu gruppieren. Aspose.Cells bietet diese Funktion auch mit der Methode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/).

## **Gruppieren von Pivot-Feldern in der Pivot-Tabelle**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716818.xlsx) und führt eine Gruppierung des ersten Pivot-Felds mit der Methode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/) durch. Anschließend aktualisiert und berechnet er die Daten der Pivot-Tabelle und speichert die Arbeitsmappe als [Ausgabedatei Excel](64716817.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispieldatei Excel. Wie im Screenshot zu sehen ist, ist das erste Pivot-Feld nun nach Monaten und Quartalen gruppiert.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}

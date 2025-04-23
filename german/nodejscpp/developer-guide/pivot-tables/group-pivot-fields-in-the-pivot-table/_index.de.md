---
title: Gruppieren von Pivot Feldern in der Pivot Tabelle
type: docs
weight: 80
url: /de/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: Wie man Pivot Felder im Pivot Table mit Aspose.Cells for Node.js via C++ gruppiert.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js Bibliothek, Wie man Pivot Felder im Pivot Table mit Aspose.Cells for Node.js via C++ gruppiert.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht das Gruppieren von Pivot-Feldern im Pivot-Table. Wenn bei einem Pivot-Feld eine große Datenmenge vorliegt, ist es oft nützlich, diese in Abschnitte zu gruppieren. Aspose.Cells for Node.js via C++ bietet dieses Feature ebenfalls mit der [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-)-Methode an.

## **Wie man Pivot-Felder in der Pivot-Tabelle gruppiert**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716818.xlsx) und führt eine Gruppierung des ersten Pivot-Felds mit der Methode [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-) durch. Anschließend aktualisiert und berechnet er die Daten der Pivot-Tabelle und speichert die Arbeitsmappe als [Ausgabedatei Excel](64716817.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispieldatei Excel. Wie im Screenshot zu sehen ist, ist das erste Pivot-Feld nun nach Monaten und Quartalen gruppiert.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}

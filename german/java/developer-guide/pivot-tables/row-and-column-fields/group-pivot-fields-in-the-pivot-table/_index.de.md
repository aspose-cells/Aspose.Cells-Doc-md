---
title: Gruppieren von Pivot Feldern in der Pivot Tabelle
type: docs
weight: 90
url: /de/java/group-pivot-fields-in-the-pivot-table/
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht es Ihnen, Pivot-Felder der Pivot-Tabelle zu gruppieren. Wenn eine große Menge Daten zu einem Pivot-Feld vorhanden ist, ist es oft nützlich, sie in Abschnitte zu gruppieren. Aspose.Cells bietet diese Funktion auch mit der Methode [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-).

## **Gruppieren von Pivot-Feldern in der Pivot-Tabelle**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716838.xlsx) und führt eine Gruppierung des ersten Pivot-Felds mit der Methode [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-) durch. Dann aktualisiert und berechnet er die Daten der Pivot-Tabelle und speichert die Arbeitsmappe als die [Ausgabe-Excel-Datei](64716837.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Wie im Screenshot zu sehen ist, ist das erste Pivot-Feld nun nach Monaten und Quartalen gruppiert.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}

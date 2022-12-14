---
title: Gruppieren Sie Pivot-Felder in der Pivot-Tabelle
type: docs
weight: 90
url: /de/java/group-pivot-fields-in-the-pivot-table/
---
## **Mögliche Nutzungsszenarien**

Microsoft In Excel können Sie Pivot-Felder der Pivot-Tabelle gruppieren. Wenn sich eine große Datenmenge auf ein Pivot-Feld bezieht, ist es oft sinnvoll, sie in Abschnitte zu gruppieren. Aspose.Cells bietet diese Funktion auch über die[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) Methode.

## **Gruppieren Sie Pivot-Felder in der Pivot-Tabelle**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716838.xlsx)und führt die Gruppierung auf dem ersten Pivot-Feld mithilfe von durch[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) Methode. Anschließend werden die Daten der Pivot-Tabelle aktualisiert und berechnet und die Arbeitsmappe als gespeichert[Excel-Datei ausgeben](64716837.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, ist das erste Pivot-Feld nun nach Monaten und Quartalen gruppiert.

![todo: Bild_alt_Text](group-pivot-fields-in-the-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}

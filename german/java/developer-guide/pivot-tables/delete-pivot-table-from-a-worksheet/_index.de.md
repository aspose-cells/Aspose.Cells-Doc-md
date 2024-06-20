---
title: Pivot Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 50
url: /de/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Möglichkeit, eine Pivot-Tabelle aus einem Arbeitsblatt zu löschen oder zu entfernen. Sie können die Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts oder der Position der Pivot-Tabelle löschen. Verwenden Sie bitte die Methode [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)), um die Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts zu löschen, und die Methode [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)), um ein Pivot-Tabellenobjekt anhand seiner Position innerhalb der Pivot-Tabelle-Sammlung zu löschen.

{{% /alert %}}

## **Beispiel**

Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zunächst wird die Pivot-Tabelle mithilfe der Methode [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) entfernt und dann wird die Pivot-Tabelle mithilfe der Methode [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) gelöscht

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}

---
title: Pivot-Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 50
url: /de/java/delete-pivot-table-from-a-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells bietet eine Funktion zum Löschen oder Entfernen einer Pivot-Tabelle aus einem Arbeitsblatt. Sie können die Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts oder der Pivot-Tabellenposition löschen. Bitte verwenden Sie die[**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable) )-Methode zum Löschen der Pivot-Tabelle mithilfe des Pivot-Tabellenobjekts und[**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int))-Methode zum Löschen eines Pivot-Tabellenobjekts anhand seiner Position innerhalb der Pivot-Tabellensammlung.

{{% /alert %}}

## **Beispiel**

 Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst entfernt es die Pivot-Tabelle mit[**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) Methode und entfernt dann die Pivot-Tabelle mit[**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) Methode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}

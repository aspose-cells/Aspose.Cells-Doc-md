---
title: Suchen und aktualisieren Sie die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle
type: docs
weight: 50
url: /de/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Mögliche Nutzungsszenarien**

Manchmal verwendet eine Pivot-Tabelle eine andere Pivot-Tabelle als Datenquelle, daher wird sie als untergeordnete Pivot-Tabelle oder verschachtelte Pivot-Tabelle bezeichnet. Sie können die untergeordneten Pivot-Tabellen einer übergeordneten Pivot-Tabelle mithilfe von finden[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) Methode.

## **Suchen und aktualisieren Sie die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](61767766.xlsx)die drei Pivot-Tabellen enthält. Die unteren beiden Pivot-Tabellen sind die Kinder der obigen Pivot-Tabelle, wie in diesem Screenshot gezeigt. Der Code findet die untergeordnete Pivot-Tabelle mithilfe von[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren())-Methode und aktualisiert sie dann nacheinander.

![todo: Bild_alt_Text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}

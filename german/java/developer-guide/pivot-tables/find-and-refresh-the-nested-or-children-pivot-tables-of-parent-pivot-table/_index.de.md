---
title: Nest oder Kind Pivot Tabellen der übergeordneten Pivot Tabelle finden und aktualisieren
type: docs
weight: 50
url: /de/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Mögliche Verwendungsszenarien**

Manchmal verwendet eine Pivot-Tabelle eine andere Pivot-Tabelle als Datenquelle, daher wird sie als untergeordnete Pivot-Tabelle oder verschachtelte Pivot-Tabelle bezeichnet. Sie können die untergeordneten Pivot-Tabellen einer übergeordneten Pivot-Tabelle unter Verwendung der [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--)-Methode finden.

## **Finden und Aktualisieren der untergeordneten oder Kind-Pivot-Tabellen der übergeordneten Pivot-Tabelle**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767766.xlsx) mit drei Pivot-Tabellen. Die unteren beiden Pivot-Tabellen sind die Untergeordneten der obigen Pivot-Tabelle, wie in diesem Screenshot gezeigt. Der Code sucht die untergeordneten Pivot-Tabellen mit der [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--)-Methode und aktualisiert sie dann nacheinander.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}

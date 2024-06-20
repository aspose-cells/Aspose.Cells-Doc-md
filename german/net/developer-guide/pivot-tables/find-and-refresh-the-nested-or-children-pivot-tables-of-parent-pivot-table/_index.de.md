---
title: Nest oder Kind Pivot Tabellen der übergeordneten Pivot Tabelle finden und aktualisieren
type: docs
weight: 60
url: /de/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Mögliche Verwendungsszenarien**

Manchmal verwendet eine Pivot-Tabelle eine andere Pivot-Tabelle als Datenquelle, daher wird sie als untergeordnete Pivot-Tabelle oder verschachtelte Pivot-Tabelle bezeichnet. Sie können die untergeordneten Pivot-Tabellen einer übergeordneten Pivot-Tabelle unter Verwendung der [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)-Methode finden.

## **Finden und Aktualisieren der untergeordneten oder Kind-Pivot-Tabellen der übergeordneten Pivot-Tabelle**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767747.xlsx), die drei Pivot-Tabellen enthält. Die unteren zwei Pivot-Tabellen sind die Kinder der obigen Pivot-Tabelle, wie in diesem Screenshot gezeigt. Der Code findet die untergeordneten Pivot-Tabellen unter Verwendung der [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)-Methode und aktualisiert sie dann nacheinander.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}

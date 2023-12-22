---
title: Suchen und aktualisieren Sie die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle
type: docs
weight: 60
url: /de/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: So finden und aktualisieren Sie die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle mit Aspose.Cells for Python via .NET.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **Mögliche Nutzungsszenarien**

Manchmal verwendet eine Pivot-Tabelle eine andere Pivot-Tabelle als Datenquelle, daher wird sie als untergeordnete Pivot-Tabelle oder verschachtelte Pivot-Tabelle bezeichnet. Sie können die untergeordneten Pivot-Tabellen einer übergeordneten Pivot-Tabelle mithilfe von finden[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)Methode.

##  **Suchen und aktualisieren Sie die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](61767747.xlsx) das drei Pivot-Tabellen enthält. Die unteren beiden Pivot-Tabellen sind die untergeordneten Elemente der obigen Pivot-Tabelle, wie in diesem Screenshot gezeigt. Der Code findet die untergeordnete Pivot-Tabelle mithilfe von[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)Methode und aktualisiert sie dann nacheinander.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}

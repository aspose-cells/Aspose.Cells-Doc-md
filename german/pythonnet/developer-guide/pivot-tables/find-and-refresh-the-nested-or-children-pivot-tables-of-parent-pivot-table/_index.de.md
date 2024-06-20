---
title: Nest oder Kind Pivot Tabellen der übergeordneten Pivot Tabelle finden und aktualisieren
type: docs
weight: 60
url: /de/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Wie man die verschachtelten oder untergeordneten Pivot Tabellen der übergeordneten Pivot Tabelle mit Aspose.Cells für Python via .NET findet und aktualisiert.
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Suchen und Aktualisieren der verschachtelten oder untergeordneten Pivot Tabellen der übergeordneten Pivot Tabelle Mit Aspose.Cells für Python Excel Bibliothek.
---

## **Mögliche Verwendungsszenarien**

Manchmal verwendet eine Pivot-Tabelle eine andere Pivot-Tabelle als Datenquelle, daher wird sie als untergeordnete Pivot-Tabelle oder verschachtelte Pivot-Tabelle bezeichnet. Sie können die untergeordneten Pivot-Tabellen einer übergeordneten Pivot-Tabelle unter Verwendung der [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)-Methode finden.

## **Wie man die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle findet und aktualisiert**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767747.xlsx), die drei Pivot-Tabellen enthält. Die unteren zwei Pivot-Tabellen sind die Kinder der obigen Pivot-Tabelle, wie in diesem Screenshot gezeigt. Der Code findet die untergeordneten Pivot-Tabellen unter Verwendung der [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)-Methode und aktualisiert sie dann nacheinander.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}

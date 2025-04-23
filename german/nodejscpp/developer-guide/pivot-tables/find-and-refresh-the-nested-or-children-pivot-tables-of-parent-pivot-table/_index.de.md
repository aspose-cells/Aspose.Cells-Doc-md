---
title: Nest oder Kind Pivot Tabellen der übergeordneten Pivot Tabelle finden und aktualisieren
type: docs
weight: 60
url: /de/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Wie man verschachtelte oder Kinder Pivot Tabellen eines übergeordneten Pivot Tabellen mit Aspose.Cells for Node.js via C++ findet und aktualisiert.
keywords: Aspose.Cells für Node.js Excel, Excel Node.js Bibliothek, Finden und Aktualisieren der verschachtelten oder Kinder Pivot Tabellen eines Eltern Pivot Tabellen mit Aspose.Cells für Node.js Excel Bibliothek.
---

## **Mögliche Verwendungsszenarien**

Manchmal verwendet eine Pivot-Tabelle eine andere Pivot-Tabelle als Datenquelle, daher wird sie als untergeordnete Pivot-Tabelle oder verschachtelte Pivot-Tabelle bezeichnet. Sie können die untergeordneten Pivot-Tabellen einer übergeordneten Pivot-Tabelle unter Verwendung der [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--)-Methode finden.

## **Wie man die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle findet und aktualisiert**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767747.xlsx), die drei Pivot-Tabellen enthält. Die unteren zwei Pivot-Tabellen sind die Kinder der obigen Pivot-Tabelle, wie in diesem Screenshot gezeigt. Der Code findet die untergeordneten Pivot-Tabellen unter Verwendung der [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--)-Methode und aktualisiert sie dann nacheinander.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}

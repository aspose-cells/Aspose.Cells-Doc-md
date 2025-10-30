---
title: Formel in Tabelle oder List Objekt automatisch propagieren, während neue Zeilen eingegeben werden
linktitle: Tabellenformel festlegen
type: docs
weight: 260
url: /de/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie, dass eine Formel in Ihrer Tabelle oder Listen-Objekt automatisch auf neue Zeilen übertragen wird, wenn Sie neue Daten eingeben. Dies ist das Standardverhalten von Microsoft Excel. Um dasselbe mit Aspose.Cells für Python via .NET zu erreichen, verwenden Sie bitte die [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula)-Eigenschaft.

## **Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden**
Der folgende Beispielcode erstellt ein Tabelle- oder List-Objekt, bei dem die Formel in Spalte B automatisch auf neue Zeilen übergeht, wenn Sie neue Daten eingeben. Bitte überprüfen Sie die [ausgegebene Excel-Datei](5115469.xlsx), die mit diesem Code generiert wurde. Wenn Sie eine beliebige Zahl in Zelle A3 eingeben, sehen Sie, dass die Formel in Zelle B2 automatisch auf Zelle B3 übergeht.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

{{< app/cells/assistant language="python-net" >}}

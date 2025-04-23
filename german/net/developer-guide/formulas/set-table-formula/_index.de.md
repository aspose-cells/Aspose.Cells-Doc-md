---
title: Formel in Tabelle oder List Objekt automatisch propagieren, während neue Zeilen eingegeben werden
linktitle: Tabellenformel festlegen
type: docs
weight: 260
url: /de/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie, dass eine Formel in Ihrer Tabelle oder Ihrem List-Objekt automatisch auf neue Zeilen übergeht, wenn neue Daten eingegeben werden. Dies ist das Standardverhalten von Microsoft Excel. Um dasselbe mit Aspose.Cells zu erreichen, verwenden Sie bitte das [ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)-Eigenschaft.
## **Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden**
Der folgende Beispielcode erstellt ein Tabelle- oder List-Objekt, bei dem die Formel in Spalte B automatisch auf neue Zeilen übergeht, wenn Sie neue Daten eingeben. Bitte überprüfen Sie die [ausgegebene Excel-Datei](5115469.xlsx), die mit diesem Code generiert wurde. Wenn Sie eine beliebige Zahl in Zelle A3 eingeben, sehen Sie, dass die Formel in Zelle B2 automatisch auf Zelle B3 übergeht.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

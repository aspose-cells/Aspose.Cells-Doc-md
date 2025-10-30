---
title: Ta bort pivottabell från ett arbetsblad
type: docs
weight: 60
url: /sv/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells for Node.js via C++ kod för att ta bort Pivot tabell för Excel Arbetsblad
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js bibliotek, ta bort pivot tabell från kalkylblad, ta bort pivot tabell från excel, hur man tar bort pivot tabell med Aspose.Cells for Node.js via C++, radera pivot tabell, ta bort pivot tabell, radera pivot tabell
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ tillhandahåller en funktion för att ta bort eller radera pivot-tabell från ett kalkylblad. Du kan ta bort pivot-tabellen med hjälp av pivot-tabell-objektet eller dess position. Använd [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-)-metoden för att ta bort pivot-tabellen med pivot-tabell-objekt och [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)-metoden för att ta bort pivot-tabell-objektet med dess position inom pivot-tabellssamlingen.

{{% /alert %}}

## **Hur man tar bort pivot-tabell från kalkylblad med Aspose.Cells for Node.js via C++**

Följande kodexempel tar bort två pivottabeller från arbetsbladet. Först tar det bort pivottabellen med hjälp av [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) -metoden och sedan tar det bort pivottabellen med hjälp av [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) -metoden

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

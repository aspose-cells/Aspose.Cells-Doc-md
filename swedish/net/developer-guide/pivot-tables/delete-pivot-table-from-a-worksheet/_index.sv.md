---
title: Ta bort pivottabell från ett arbetsblad
type: docs
weight: 60
url: /sv/net/delete-pivot-table-from-a-worksheet/
description: C# kod för att ta bort PivotTable för Excel ark
keywords: c# ta bort pivottabell från arbetsblad, c# ta bort pivottabell från excel, hur man tar bort pivottabell med c#, ta bort pivottabell med c#, ta bort pivottabell från excel med c#, c# ta bort pivottabell, c# ta bort pivottabell, ta bort pivottabell, ta bort pivottabell, hur man tar bort pivottabell
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en funktion för att radera eller ta bort pivottabell från ett arbetsblad. Du kan ta bort pivottabellen med hjälp av pivottabellobjektet eller pivottabellens position. Använd [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) -metoden för att ta bort pivottabellen med hjälp av pivottabellobjektet och [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) metoden för att ta bort pivottabellen med hjälp av dess position i pivottabellssamlingen.

{{% /alert %}}

Följande kodexempel tar bort två pivottabeller från arbetsbladet. Först tar det bort pivottabellen med hjälp av [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) -metoden och sedan tar det bort pivottabellen med hjälp av [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) -metoden

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}

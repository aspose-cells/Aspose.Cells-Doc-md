---
title: Ta bort pivottabell från ett kalkylblad
type: docs
weight: 60
url: /sv/net/delete-pivot-table-from-a-worksheet/
description: C#-kod för att ta bort PivotTable för Excel-kalkylblad
keywords: c# remove pivot table from worksheet, c# remove pivot table from excel, how to delete pivot table with c#, delete pivot table with c#, delete pivot table from excel with c#, c# delete pivot table, c# remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller en funktion för att ta bort eller ta bort pivottabell från ett kalkylblad. Du kan ta bort pivottabellen med pivottabellobjekt eller pivottabellposition. Vänligen använd[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) metod för att ta bort pivottabellen med pivottabellobjekt och[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) metod för att ta bort pivottabellobjekt med dess position i pivottabellsamlingen.

{{% /alert %}}

 Följande exempelkod tar bort två pivottabeller från kalkylbladet. Först tar den bort pivottabellen med hjälp av[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) metod och sedan tar den bort pivottabellen med hjälp av[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) metod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}

---
title: Ta bort pivottabell från ett kalkylblad
type: docs
weight: 60
url: /sv/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET kod för att ta bort pivottabell för Excel-kalkylblad
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET tillhandahåller en funktion för att ta bort eller ta bort pivottabell från ett kalkylblad. Du kan ta bort pivottabellen med pivottabellobjekt eller pivottabellposition. Vänligen använd[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) metod för att ta bort pivottabellen med pivottabellobjekt och[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)metod för att ta bort pivottabellobjekt med dess position i pivottabellsamlingen.

{{% /alert %}}

 Följande exempelkod tar bort två pivottabeller från kalkylbladet. Först tar den bort pivottabellen med hjälp av[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) metod och sedan tar den bort pivottabellen med hjälp av[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) metod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}

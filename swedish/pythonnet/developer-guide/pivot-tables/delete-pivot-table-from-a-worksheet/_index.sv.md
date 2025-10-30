---
title: Ta bort pivottabell från ett arbetsblad
type: docs
weight: 60
url: /sv/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET kod för att ta bort PivotTable för Excel ark
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Python via .NET tar bort pivot tabell från kalkylblad, Python via .NET tar bort pivot tabell från excel, hur man tar bort pivot tabell med Python via .NET, ta bort pivot tabell med Python via .NET, ta bort pivot tabell från excel med Python via .NET, Python via .NET ta bort pivot tabell, Python via .NET ta bort pivot tabell, ta bort pivot tabell, ta bort pivot tabell, hur man tar bort pivot tabell
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET ger en funktion för att ta bort eller ta bort pivot-tabell från en arbetsbok. Du kan ta bort pivot-tabellen med hjälp av pivot-tabellobjekt eller pivot-tabellposition. Använd [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/)-metoden för att ta bort pivot-tabellen med pivot-tabellobjekt och [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)-metoden för att ta bort pivot-tabellobjekt med sin position inuti pivot-tabellkollektionen.

{{% /alert %}}

## **Hur man tar bort pivot-tabell från kalkylblad med hjälp av Aspose.Cells för Python Excel Library**

Följande kodexempel tar bort två pivottabeller från arbetsbladet. Först tar det bort pivottabellen med hjälp av [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) -metoden och sedan tar det bort pivottabellen med hjälp av [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) -metoden

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}

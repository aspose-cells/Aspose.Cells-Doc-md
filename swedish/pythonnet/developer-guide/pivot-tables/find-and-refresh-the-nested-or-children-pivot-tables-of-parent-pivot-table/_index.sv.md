---
title: Hitta och uppdatera pivottabellerna för kapslade eller barn i överordnade pivottabeller
type: docs
weight: 60
url: /sv/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Så här hittar och uppdaterar du kapslade eller underordnade pivottabeller för överordnad pivottabell med Aspose.Cells for Python via .NET.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **Möjliga användningsscenarier**

Ibland använder en pivottabell en annan pivottabell som datakälla, så den kallas en underordnad pivottabell eller kapslad pivottabell. Du kan hitta de underordnade pivottabellerna för en överordnad pivottabell med hjälp av[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)metod.

##  **Hitta och uppdatera pivottabellerna för kapslade eller barn i överordnade pivottabeller**

 Följande exempelkod laddar[exempel på Excel-fil](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottabellerna är underordnade av ovanstående pivottabell som visas i den här skärmdumpen. Koden hittar pivottabellen för barn med hjälp av[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)och uppdaterar dem sedan en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}

---
title: Hitta och uppdatera pivottabellerna för kapslade eller barn i överordnade pivottabeller
type: docs
weight: 60
url: /sv/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Möjliga användningsscenarier**

Ibland använder en pivottabell en annan pivottabell som datakälla, så den kallas en underordnad pivottabell eller kapslad pivottabell. Du kan hitta de underordnade pivottabellerna för en överordnad pivottabell med hjälp av[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)metod.

## **Hitta och uppdatera pivottabellerna för kapslade eller barn i överordnade pivottabeller**

 Följande exempelkod laddar[exempel på Excel-fil](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottabellerna är underordnade av ovanstående pivottabell som visas i den här skärmdumpen. Koden hittar pivottabellen för barn med hjälp av[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)och uppdaterar dem sedan en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}

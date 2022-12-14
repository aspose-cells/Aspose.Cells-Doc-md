---
title: Hitta och uppdatera pivottabellerna för kapslade eller barn i överordnade pivottabeller
type: docs
weight: 50
url: /sv/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Möjliga användningsscenarier**

Ibland använder en pivottabell en annan pivottabell som datakälla, så den kallas en underordnad pivottabell eller kapslad pivottabell. Du kan hitta de underordnade pivottabellerna för en överordnad pivottabell med hjälp av[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) metod.

## **Hitta och uppdatera pivottabellerna för kapslade eller barn i överordnade pivottabeller**

Följande exempelkod laddar[exempel på Excel-fil](61767766.xlsx)som innehåller tre pivottabeller. De två nedre pivottabellerna är underordnade av ovanstående pivottabell som visas i den här skärmdumpen. Koden hittar pivottabellen för barn med hjälp av[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) och uppdaterar dem sedan en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}

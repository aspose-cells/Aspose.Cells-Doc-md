---
title: Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen
type: docs
weight: 50
url: /sv/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Möjliga användningsscenario**

Ibland använder en pivottabell en annan pivottabell som datakälla, så det kallas en underordnad pivottabell eller inbäddad pivottabell. Du kan hitta de underordnade pivottablerna i en föräldrapivottabell med hjälp av [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) metoden.

## **Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen**

Följande kodexempel laddar [provexfilsnamn](61767766.xlsx) som innehåller tre pivot-tabeller. De nedre två pivot-tabellerna är barnen till ovanstående pivot-tabell som visas i denna skärmdump. Koden hittar barnpivot-tabellen med hjälp av [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) metoden och uppdaterar dem en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
{{< app/cells/assistant language="java" >}}

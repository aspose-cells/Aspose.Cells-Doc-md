---
title: Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen
type: docs
weight: 60
url: /sv/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Möjliga användningsscenario**

Ibland använder en pivottabell en annan pivottabell som datakälla, så det kallas en underordnad pivottabell eller inbäddad pivottabell. Du kan hitta de underordnade pivottablerna i en föräldrapivottabell med hjälp av [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) metoden.

## **Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen**

Följande kod laddar den [prov-Eexcelfilen](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottablerna är barn till den ovanstående pivottabellen som visas i denna skärmdump. Koden hittar de underordnade pivottablerna med hjälp av [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) metoden och uppdaterar dem en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
{{< app/cells/assistant language="csharp" >}}

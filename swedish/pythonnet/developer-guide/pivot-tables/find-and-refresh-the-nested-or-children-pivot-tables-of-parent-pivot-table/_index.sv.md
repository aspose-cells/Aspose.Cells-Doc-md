---
title: Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen
type: docs
weight: 60
url: /sv/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Hur man hittar och uppdaterar de inbäddade eller barnpivot tabellerna till föräldrapivot tabell med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Hitta och uppdatera de inbäddade eller barnpivot tabellerna till föräldrapivot tabell med hjälp av Aspose.Cells för Python Excel Library.
---

## **Möjliga användningsscenario**

Ibland använder en pivottabell en annan pivottabell som datakälla, så det kallas en underordnad pivottabell eller inbäddad pivottabell. Du kan hitta de underordnade pivottablerna i en föräldrapivottabell med hjälp av [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) metoden.

## **Här demonstreras funktionen med följande provkod genom att ladda den [prov-Excel-filen](61767747.xlsx) som innehåller tre pivot-tabeller. De två nedre pivot-tabellerna är barn till ovanstående pivot-tabell enligt visas i denna skärmbild. Koden hittar barnpivot-tabellerna med hjälp av {0}-metoden och sedan uppdaterar dem en efter en.**

Följande kod laddar den [prov-Eexcelfilen](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottablerna är barn till den ovanstående pivottabellen som visas i denna skärmdump. Koden hittar de underordnade pivottablerna med hjälp av [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) metoden och uppdaterar dem en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}

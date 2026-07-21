---
title: Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen
type: docs
weight: 60
url: /sv/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Hur man hittar och uppdaterar inbäddade eller barnpivottabeller av föräldrapivottabell med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells för Node.js Excel, Node.js Excel bibliotek, Hitta och uppdatera inbäddade eller barnpivottabeller av föräldrapivottabell med Aspose.Cells för Node.js Excel bibliotek.
---

## **Möjliga användningsscenario**

Ibland använder en pivottabell en annan pivottabell som datakälla, så det kallas en underordnad pivottabell eller inbäddad pivottabell. Du kan hitta de underordnade pivottablerna i en föräldrapivottabell med hjälp av [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) metoden.

## **Här demonstreras funktionen med följande provkod genom att ladda den [prov-Excel-filen](61767747.xlsx) som innehåller tre pivot-tabeller. De två nedre pivot-tabellerna är barn till ovanstående pivot-tabell enligt visas i denna skärmbild. Koden hittar barnpivot-tabellerna med hjälp av {0}-metoden och sedan uppdaterar dem en efter en.**

Följande kod laddar den [prov-Eexcelfilen](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottablerna är barn till den ovanstående pivottabellen som visas i denna skärmdump. Koden hittar de underordnade pivottablerna med hjälp av [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) metoden och uppdaterar dem en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

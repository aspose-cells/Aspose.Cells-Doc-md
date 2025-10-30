---
title: Hitta och uppdatera inbäddade eller barnpivottabeller av föräldrapivot med Golang via C++
linktitle: Hitta och uppdatera inbäddade eller barnpivot tabeller
type: docs
weight: 60
url: /sv/go-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Lär dig hur man hittar och uppdaterar inbäddade eller barnpivot tabeller av en föräldrapivot tabell med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland använder en pivottabell en annan pivottabell som datakälla, så det kallas en underordnad pivottabell eller inbäddad pivottabell. Du kan hitta de underordnade pivottablerna i en föräldrapivottabell med hjälp av [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/) metoden.

## **Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen**

Följande kod laddar den [prov-Eexcelfilen](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottablerna är barn till den ovanstående pivottabellen som visas i denna skärmdump. Koden hittar de underordnade pivottablerna med hjälp av [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/) metoden och uppdaterar dem en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindAndRefreshTheNestedOrChildrenPivotTablesOfParentPivotTable.go" >}}

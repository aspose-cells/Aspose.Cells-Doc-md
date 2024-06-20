---
title: Namn och Index
type: docs
weight: 10
url: /sv/cpp/names-and-indices/
---

## **Hämta cellnamn från rad- och kolumnindex**
Det är möjligt att hitta ett cells namn med rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells tillhandahåller metoden [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/), vilket tillåter utvecklare att få cellens namn om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells att räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande kodexempel illustrerar hur man använder [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) för att komma åt en cells namn med ett känt rad- och kolumnindex. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **Hämta rad- och kolumnindex från cellens namn**
Det är möjligt att hitta en rad- och kolumnindex för cellen från dess namn. Denna artikel förklarar hur.
Aspose.Cells tillhandahåller metoden [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/), vilket tillåter utvecklare att hämta rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells att räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande kodexempel illustrerar hur man använder [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) för att hämta rad- och kolumnindex från cellens namn. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}

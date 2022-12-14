---
title: Namn och index
type: docs
weight: 10
url: /sv/cpp/names-and-indices/
---
## **Hämta Cell Namn från rad- och kolumnindex**
Det är möjligt att hitta en cells namn med tanke på rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells tillhandahåller metoden ICellsHelper.CellIndexToName_i som tillåter utvecklare att få en cells namn om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur du använder ICellsHelper.CellIndexToName_i för att komma åt en cells namn givet ett känt rad- och kolumnindex. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Hämta rad- och kolumnindex från Cell Namn**
Det är möjligt att hitta ett rad- och kolumnindex för cellen från dess namn. Den här artikeln förklarar hur.
Aspose.Cells tillhandahåller metoden ICellsHelper.CellNameToIndex_i som tillåter utvecklare att hämta ett rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur du använder CellsHelper.CellNameToIndex för att hämta rad- och kolumnindex från cellens namn. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}

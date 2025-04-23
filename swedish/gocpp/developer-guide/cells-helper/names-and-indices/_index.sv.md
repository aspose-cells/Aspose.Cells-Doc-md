---
title: Namn och Index
type: docs
weight: 10
url: /sv/go-cpp/names-and-indices/
---

## **Hämta cellnamn från rad- och kolumnindex**

Det är möjligt att hitta ett cells namn med rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells tillhandahåller metoden [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/), som gör det möjligt för utvecklare att få namnet på en cell om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}}

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells att räkna rad- och kolumnindex från 0.

{{% /alert %}}

 Följande exempel visar hur man använder [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/) för att få tillgång till ett cells namn givet ett känt rad- och kolumnindex. Koden genererar följande utskrifter.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **Hämta rad- och kolumnindex från cellens namn**

Det är möjligt att hitta en rad- och kolumnindex för cellen från dess namn. Denna artikel förklarar hur.
Aspose.Cells tillhandahåller metoden [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/), som gör det möjligt för utvecklare att få ett rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}}

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells att räkna rad- och kolumnindex från 0.

{{% /alert %}}

 Följande exempel visar hur man använder [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/) för att få rad- och kolumnindex från cellens namn. Koden genererar följande utskrifter.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}

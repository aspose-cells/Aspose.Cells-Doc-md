---
title: Hämta Cells Index
type: docs
weight: 600
url: /sv/net/get-cells-index/
description: Lär dig hur du får in rad eller kolumn med namnet på rad , kolumn eller celler. Konvertera namnet på cellen till rad- och kolumnindex nollbaserat.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
Standardvyn i Excel är A1-stilreferens, varje kolumn är definierad som A, B, C.... och cellerna namnges som A1, B2, C3... och så vidare.
Du kanske vill veta vilken rad och kolumn den här cellen befinner sig i.

{{% /alert %}}


##  **Möjliga användningsscenarier**
 När du bara behöver manipulera en specifik data på kalkylbladet efter rad och kolumnindex, måste du känna till kolumn- och kolumnindexen för den specifika cellen.
 Aspose.Cells erbjuder den här funktionen för att få rad- och kolumnindex efter namnet på raden, kolumnen och cellen.
Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Obs: Indexeringen är nollbaserad i Aspose.Cells för .Net, men ID för Row är en-baserad i MS Excel.

##  **Få Cells-index med Aspose.Cells**
Det här exemplet visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hitta den specifika cellen i det första kalkylbladet.
1. Hämta radindex och kolumnindex efter cellens namn.
1. Hämta kolumnindex efter namnet på kolumnen.
1. Hämta radindex efter namnet på raden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
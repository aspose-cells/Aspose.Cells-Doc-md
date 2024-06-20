---
title: Få cellerindex
type: docs
weight: 600
url: /sv/net/get-cells-index/
description: Lär dig hur man får rad eller kolumn genom namnet på raden, kolumnen eller cellerna. Konvertera namnet på cellen till rad och kolumnindex nollbaserat.
keywords: Få radindex och kolumnindex efter namnet på cellen, Få kolumnindex efter namnet på kolumnen, Få radindex efter namnet på raden, Få index efter namnet på cellen. 
---

{{% alert color="primary" %}}
Standardvyn i Excel är A1-stilreferens, där varje kolumn är definierad som A, B, C ... och cellerna namnges som A1, B2, C3 ... och så vidare.
Du kan vilja veta vilken rad och kolumn är denna cell i.

{{% /alert %}}


## **Möjliga användningsscenario**
När du bara behöver manipulera en specifik data på arbetsbladet genom rad- och kolumnindex behöver du veta kolumn- och kolumnindex för den specifika cellen. 
Aspose.Cells erbjuder denna funktion för att få rad- och kolumnindex efter namnet på raden, kolumnen och cellen. 
Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Observera: Indexeringen är nollbaserad i Aspose.Cells för .Net, men ID för rad är baserat på ett i MS Excel.

## **Få cellers index med hjälp av Aspose.Cells**
Detta exempel visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hitta den specifika cellen i det första arbetsbladet.
1. Få radindex och kolumnindex efter namnet på cellen.
1. Få kolumnindex efter namnet på kolumnen.
1. Få radindex efter namnet på raden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}

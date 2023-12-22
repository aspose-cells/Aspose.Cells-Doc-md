---
title: Få Max Column Index i rad och Max Row Index i kolumn
type: docs
weight: 600
url: /sv/net/get-max-index-in-row-and-column/
description: Lär dig hur du får Max Column Index i rad och Max Row Index i kolumn genom Aspose.Cells for .NET API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **Möjliga användningsscenarier**
När du bara behöver manipulera vissa data på raderna eller kolumnerna måste du känna till dataintervallet för rader och kolumner. Aspose.Cells erbjuder denna funktion. För att få det maximala kolumnindexet på en rad kan du få[Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) och[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) egenskaper och använd sedan[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) egenskap för att få maximalt kolumnindex och maximalt datakolumnindex. Men för att erhålla det maximala radindexet och det maximala raddataindexet i en kolumn måste du skapa ett intervall i kolumnen, sedan gå igenom intervallet för att hitta den sista cellen och slutligen få[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attribut på cellen.

Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Få Max Column Index i rad och Max Row Index i kolumn med Aspose.Cells**
Det här exemplet visar hur man:

1.  Ladda[exempelfil](sample.xlsx).
1. Hämta raden som behöver få maximalt kolumnindex och maximalt datakolumnindex.
1.  Skaffa sig[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) attribut på cellen.
1. Skapa ett intervall baserat på kolumn.
1. Skaffa iterator och traversering.
1.  Skaffa sig[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attribut på cellen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
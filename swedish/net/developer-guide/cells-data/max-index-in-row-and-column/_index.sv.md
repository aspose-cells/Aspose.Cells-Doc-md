---
title: Hämta maximal kolumnindex i rad och maximal radindex i kolumn
type: docs
weight: 600
url: /sv/net/get-max-index-in-row-and-column/
description: Lär dig hur man får Maximalt Kolumnindex i Rad och Maximalt Radindex i Kolumn genom Aspose.Cells for .NET API.
keywords: Få Maximalt Kolumnindex i Rad, få Maximalt Radindex i Kolumn, få Maximalt Datakolumnindex i Rad, få Maximalt Dataradindex i Kolumn. 
---

## **Möjliga användningsscenario**
När du endast behöver manipulera en del data på raderna eller kolumnerna behöver du veta dataområdet för rader och kolumner. Aspose.Cells erbjuder denna funktion. För att skaffa det maximala kolumnindexet på en rad kan du skaffa [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) och [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) egenskaperna, och sedan använda [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) egenskapen för att skaffa det maximala kolumnindexet och maximala datakolumnindexet. Men för att skaffa det maximala radindexet och maximala raddataindexet på en kolumn behöver du skapa ett område på kolumnen, sedan traversera området för att hitta den sista cellen, och slutligen skaffa [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attributet på cellen.

Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Få Maximalt Kolumnindex i Rad och Maximalt Radindex i Kolumn med hjälp av Aspose.Cells**
Detta exempel visar hur man:

1. Ladda in [provfilen](sample.xlsx).
1. Hämta raden som behöver få det maximala kolumnindexet och det maximala datakolumnindexet.
1. Hämta [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) attributet på cellen.
1. Skapa ett intervall baserat på kolumn.
1. Hämta iteratorn och traversera intervallen.
1. Hämta [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attribut på cellen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}

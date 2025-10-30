---
title: Hämta maximal kolumnindex i rad och maximal radindex i kolumn med Golang via C++
linktitle: Hämta maximal kolumnindex i rad och maximal radindex i kolumn
type: docs
weight: 600
url: /sv/go-cpp/get-max-index-in-row-and-column/
description: Lär dig hur du hämtar maximalt kolumnindex i rad och maximalt radindex i kolumn via API et Aspose.Cells for C++.
keywords: Få Maximalt Kolumnindex i Rad, få Maximalt Radindex i Kolumn, få Maximalt Datakolumnindex i Rad, få Maximalt Dataradindex i Kolumn.
---

## **Möjliga användningsscenario**
När du bara behöver manipulera vissa data på rader eller kolumner, behöver du känna till dataintervallet för rader och kolumner. Aspose.Cells erbjuder denna funktion. För att få det maximala kolumnindexet i en rad kan du hämta [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) och [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), och sedan använda egenskapen [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) för att få det maximala kolumnindexet och det maximala data kolumnindexet. Men för att få det maximala radindexet och det maximala raddataindexet i en kolumn, måste du skapa ett område på kolumnen, sedan traversera detta område för att hitta den sista cellen, och slutligen få attributet [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) på cellen.

Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Få Maximalt Kolumnindex i Rad och Maximalt Radindex i Kolumn med hjälp av Aspose.Cells**
Detta exempel visar hur man:

1. Ladda in [provfilen](sample.xlsx).
1. Hämta raden som behöver få det maximala kolumnindexet och det maximala datakolumnindexet.
1. Hämta [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) attribut på cellen.
1. Skapa ett intervall baserat på kolumn.
1. Hämta iteratorn och traversera intervallen.
1. Hämta [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) attribut på cellen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}

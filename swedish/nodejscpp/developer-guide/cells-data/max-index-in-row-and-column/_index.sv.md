---
title: Hämta maximal kolumnindex i rad och maximal radindex i kolumn
type: docs
weight: 600
url: /sv/nodejs-cpp/get-max-index-in-row-and-column/
description: Lär dig hur du får maximal kolumnindex i rad och maximal radindex i kolumn via Aspose.Cells for Node.js via C++ API.
keywords: Få maximal kolumnindex i rad Node.js via C++, Få maximal radindex i kolumn Node.js via C++, Få maximal datakolumnindex i rad Node.js via C++, Få maximal data radindex i kolumn Node.js via C++.
---

## **Möjliga användningsscenario**
När du bara behöver manipulera viss data på rader eller kolumner, behöver du känna till dataintervallet för rader och kolumner. Aspose.Cells for Node.js via C++ erbjuder denna funktion. För att erhålla det maximala kolumnindexet på en rad kan du använda [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) och [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--) metoderna, och sedan använda [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) metoden för att få det maximala kolumnindexet och maximala datakolumnindexet. Men för att få det maximala radindexet och maximalt data radindex på en kolumn måste du skapa ett intervall på kolumnen, sedan traversera intervallet för att hitta den sista cellen, och slutligen anropa [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) metoden på cellen.

Aspose.Cells for Node.js via C++ tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Få Max kolumnindex i rad och Max radindex i kolumn**
Detta exempel visar hur man:

1. Ladda in [provfilen](sample.xlsx).
1. Hämta raden som behöver få det maximala kolumnindexet och det maximala datakolumnindexet.
1. Anropa [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) metoden på cellen.
1. Skapa ett intervall baserat på kolumn.
1. Hämta iteratorn och traversera intervallen.
1. Anropa [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) metoden på cellen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}

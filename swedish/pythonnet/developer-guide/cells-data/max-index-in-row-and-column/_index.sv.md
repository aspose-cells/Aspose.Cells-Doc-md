---
title: Hämta maximal kolumnindex i rad och maximal radindex i kolumn
type: docs
weight: 600
url: /sv/python-net/get-max-index-in-row-and-column/
description: Lär dig hur man hämtar maximal kolumnindex i rad och maximal radindex i kolumn genom Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python Hämta maximal kolumnindex i rad, Python Hämta maximal radindex i kolumn, Python Hämta maximalt datakolumnindex i rad, Python Hämta maximalt dataradindex i kolumn 
---

## **Möjliga användningsscenario**
När du bara behöver manipulera viss data på raderna eller kolumnerna behöver du veta dataomfånget för raderna och kolumnerna. Aspose.Cells for Python via .NET erbjuder denna funktion. för att få det maximala kolumnindexet på en rad kan du få egenskaperna [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) och [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/) och sedan använda egenskapen [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) för att få det maximala kolumnindexet och maximala datakolumnindexet. Men för att få maximala radindex och maximala rad dataindex i en kolumn måste du skapa ett intervall på kolumnen, sedan traversera intervallet för att hitta det sista cellen, och slutligen få attributet [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) för cellen.

Aspose.Cells för Python via .NET tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Hämta Max kolumnindex i rad och Max radindex i kolumn med hjälp av Aspose.Cells för Python Excel Library**
Detta exempel visar hur man:

1. Ladda in [provfilen](sample.xlsx).
1. Hämta raden som behöver få det maximala kolumnindexet och det maximala datakolumnindexet.
1. Hämta [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) attributet på cellen.
1. Skapa ett intervall baserat på kolumn.
1. Hämta iteratorn och traversera intervallen.
1. Hämta [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) attributet på cellen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}

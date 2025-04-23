---
title: Hämta maximalt kolumnindex i rad och maximalt radindex i kolumn med C++
linktitle: Hämta maximal kolumnindex i rad och maximal radindex i kolumn
type: docs
weight: 600
url: /sv/cpp/get-max-index-in-row-and-column/
description: Lär dig hur du hämtar maximalt kolumnindex i rad och maximalt radindex i kolumn via API et Aspose.Cells for C++.
keywords: Få Maximalt Kolumnindex i Rad, få Maximalt Radindex i Kolumn, få Maximalt Datakolumnindex i Rad, få Maximalt Dataradindex i Kolumn.
---

## **Möjliga användningsscenario**
När du bara behöver manipulera viss data i rader eller kolumner, behöver du veta dataintervallet för rader och kolumner. Aspose.Cells erbjuder denna funktion. För att få det maximala kolumnindexet på en rad kan du använda egenskaperna [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) och [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), och därefter använda egenskapen [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) för att få det maximala kolumnindexet och det maximala datakolumnindexet. Men för att få det maximala radindexet och maximala dataradindexet på en kolumn måste du skapa ett område på kolumnen, sedan traversera området för att hitta den sista cellen, och slutligen hämta egenskapen [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) för cellen.

Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Få Maximalt Kolumnindex i Rad och Maximalt Radindex i Kolumn med hjälp av Aspose.Cells**
Detta exempel visar hur man:

1. Ladda in [provfilen](sample.xlsx).
1. Hämta raden som behöver få det maximala kolumnindexet och det maximala datakolumnindexet.
1. Hämta [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) egenskap på cellen.
1. Skapa ett intervall baserat på kolumn.
1. Hämta iteratorn och traversera intervallen.
1. Hämta [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) egenskap på cellen.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

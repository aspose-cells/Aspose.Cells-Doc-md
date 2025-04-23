---
title: Hämta cellernas index med C++
linktitle: Få cellerindex
type: docs
weight: 600
url: /sv/cpp/get-cells-index/
description: Lär dig hur man får rad eller kolumnindex efter namnet på rad, kolumn eller cell. Konvertera cellnamnet till rad och kolumnindex med nollbaserat index med Aspose.Cells och C++.
keywords: Få radindex och kolumnindex efter namnet på cellen, Få kolumnindex efter namnet på kolumnen, Få radindex efter namnet på raden, Få index efter namnet på cellen.
---

{{% alert color="primary" %}}
Standardvyn i Excel är A1-stilreferens, där varje kolumn definieras som A, B, C.... och cellerna heter A1, B2, C3... och så vidare.
 Du kanske vill veta vilken rad och kolumn denna cell befinner sig i.

{{% /alert %}}

## **Möjliga användningsscenario**
 När du bara behöver manipulera specifika data på arket efter rad- och kolumnindex, behöver du känna till rad- och kolumnindex för den specifika cellen. 
Aspose.Cells erbjuder denna funktion för att få rad- och kolumnindex efter namnet på raden, kolumnen och cellen. 
Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål:
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

Observera: Indexeringen är nollbaserad i Aspose.Cells for C++, men Row-ID är 1-baskat i MS Excel.

## **Få cellers index med hjälp av Aspose.Cells**
Detta exempel visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hitta den specifika cellen i det första arbetsbladet.
1. Få radindex och kolumnindex efter namnet på cellen.
1. Få kolumnindex efter namnet på kolumnen.
1. Få radindex efter namnet på raden.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

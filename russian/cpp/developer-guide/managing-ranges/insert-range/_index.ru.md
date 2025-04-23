---  
title: Вставить диапазоны в Excel с помощью C++  
linktitle: Вставка диапазонов  
type: docs  
weight: 105  
url: /ru/cpp/insert-ranges-to-excel/  
description: Узнайте, как вставлять диапазоны в файлы Excel с помощью Aspose.Cells и C++.  
---  

## **Введение**

В Excel можно выбрать диапазон, а затем вставить диапазон и сдвинуть другие данные вправо или вниз.

**![Опции сдвига](InsertRange.png)**

## **Вставка диапазонов с помощью Aspose.Cells**

Aspose.Cells предоставляет метод [Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/), чтобы вставлять диапазон.

## **Вставка диапазонов и сдвиг ячеек вправо**

Вставить диапазон и сдвинуть ячейки вправо, как показано в кодах с Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into a few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    CellArea ca = CellArea::CreateCellArea(u"A1", u"A2");
    worksheet.GetCells().InsertRange(ca, ShiftType::Right);

    std::cout << (worksheet.GetCells().Get(u"B1").GetStringValue() == u"Test" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вставка диапазонов и сдвиг ячеек вниз**

Вставить диапазон и сдвинуть ячейки вниз, как показано в кодах с Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // a few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(u"123");
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A2");
    worksheet.GetCells().InsertRange(ca, ShiftType::Down);

    std::cout << (worksheet.GetCells().Get(u"A3").GetStringValue() == u"Test" ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```


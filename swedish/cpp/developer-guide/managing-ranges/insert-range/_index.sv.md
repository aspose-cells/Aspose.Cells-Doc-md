---  
title: Infoga intervall i Excel med C++  
linktitle: Infoga intervall  
type: docs  
weight: 105  
url: /sv/cpp/insert-ranges-to-excel/  
description: Lär dig hur man infogar områden i Excelfiler med Aspose.Cells i C++.  
---  

## **Introduktion**

I Excel kan du välja ett intervall, sedan infoga ett intervall och skifta andra data höger eller ned.

**![Skiftalternativ](InsertRange.png)**

## **Infoga Intervall med Aspose.Cells**

Aspose.Cells tillhandahåller metoden [Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/) för att infoga ett område.

## **Infoga Intervall och skifta celler höger**

Infoga ett område och skjut cellerna till höger med följande kodexempel med Aspose.Cells:

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

## **Infoga Intervall och skifta celler ned**

Infoga ett område och skjut cellerna nedåt med följande kodexempel med Aspose.Cells:

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


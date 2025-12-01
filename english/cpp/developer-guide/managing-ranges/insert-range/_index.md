---  
title: Insert Ranges to Excel with C++  
linktitle: Insert Ranges  
type: docs  
weight: 105  
url: /cpp/insert-ranges-to-excel/  
description: Learn how to insert ranges into Excel files using Aspose.Cells with C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Introduction**

In Excel, you can select a range, then insert a range and shift other data right or down.

**![Shift options](InsertRange.png)**

## **Insert Ranges Using Aspose.Cells**

Aspose.Cells provides [Cells.InsertRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrange/) method to insert a range.

## **Insert Ranges And Shift Cells Right**

Insert a range and shift cells right as the following codes with Aspose.Cells:

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

## **Insert Ranges And Shift Cells Down**

Insert a range and shift cells down as the following codes with Aspose.Cells:

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

{{< app/cells/assistant language="cpp" >}}

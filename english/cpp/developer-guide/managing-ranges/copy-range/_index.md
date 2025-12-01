--- 
title: Copy Ranges of Excel with C++ 
linktitle: Copy Ranges 
type: docs 
weight: 105 
url: /cpp/copy-ranges-of-excel/ 
description: Learn how to copy ranges in Excel using Aspose.Cells with C++. 
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
--- 

## **Introduction**

In Excel, you can select a range, copy the range, then paste it with specific options to the same worksheet, other worksheets or other files.

## **Copy Ranges Using Aspose.Cells**

Aspose.Cells provides some overload [Range.Copy](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) methods to copy the range. And [Range.CopyStyle](https://reference.aspose.com/cells/cpp/aspose.cells/range/copystyle/) only the copy style of the range; [Range.CopyData](https://reference.aspose.com/cells/cpp/aspose.cells/range/copydata/) only the copy value of the range.

## **Copy Range**

Creating two ranges: the source range, the target range, then copying source range to target range with Range.Copy method.

See the following code:

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

    // Input some data with some formattings into
    // A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy source range to target range in the same worksheet 
    targetRange.Copy(sourceRange);

    // Create a new worksheet.
    worksheets.Add();
    worksheet = worksheets.Get(1);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another worksheet 
    targetRange.Copy(sourceRange);

    // Copy to another workbook
    Workbook anotherWorkbook;

    worksheet = workbook.GetWorksheets().Get(0);
    
    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another workbook 
    targetRange.Copy(sourceRange);
    
    std::cout << "Copy operations completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Paste Range With Options**

Aspose.Cells supports pasting the range with specific type.

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

    // Input some data with some formattings into A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Init paste options.
    PasteOptions options;
    // Set paste type.
    options.SetPasteType(PasteType::ValuesAndFormats);
    options.SetSkipBlanks(true);

    // Copy source range to target range
    targetRange.Copy(sourceRange, options);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Only Copy Data Of The Range**
Also you can copy the data with Range.CopyData method as the following codes:

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
    // A few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(123);

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy the data of source range to target range
    targetRange.CopyData(sourceRange);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Copy Row Heights of Source Range to Destination Range](/cells/cpp/copy-row-heights-of-source-range-to-destination-range/)
{{< app/cells/assistant language="cpp" >}}

---
title: Get Text Width of Cell Value with C++
linktitle: Get Text Width of Cell Value
type: docs
weight: 50
url: /cpp/get-text-width-of-cell-value/
description: Learn how to get Text Width of Cell Value through the Aspose.Cells for C++ API.
keywords: Get Text Width of Cell Value, Obtain Text Width of Cell Value
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Text Width of Cell Value**

Sometimes developers might need to calculate the width of a cell's value for arranging data in a layout. Aspose.Cells provides the [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) method which allows developers to get the text width of the cell's value. The following sample code illustrates how to use [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) to access the text width of the cell's value.

The source file used in the following code snippet is attached for your reference.

[Source File](96928090.xlsx)

## Sample Code

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(),
                                                workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

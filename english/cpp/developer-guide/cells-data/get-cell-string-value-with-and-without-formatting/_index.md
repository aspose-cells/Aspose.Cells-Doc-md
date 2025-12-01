---
title: Get Cell String Value with and without Formatting with C++
linktitle: Get Cell String Value
type: docs
weight: 240
url: /cpp/get-cell-string-value-with-and-without-formatting/
description: Learn how to Get Cell String Value with and without Formatting through the Aspose.Cells for C++ API.
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides a method [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) which can be used to get the string value of the cell with or without any formatting. Suppose, you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) method. It takes [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) enum as a parameter which has the following values:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

The following sample code explains the use of [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) method.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell to display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Get string value as Cell Style
    U16String value = cell.GetStringValue(CellValueFormatStrategy::CellStyle);
    std::cout << value.ToUtf8() << std::endl;

    // Get string value without any formatting
    value = cell.GetStringValue(CellValueFormatStrategy::None);
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}

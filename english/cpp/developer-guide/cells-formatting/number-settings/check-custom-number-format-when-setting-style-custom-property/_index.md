---
title: Check Custom Number Format when Setting Style.Custom Property with C++
description: Aspose.Cells is a C++ library for working with spreadsheet files, which supports checking custom number formats when styling. This article will show you how to use the Aspose.Cells library to check custom number formats to ensure that the styling is correct.
keywords: Aspose.Cells, C++ libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /cpp/check-custom-number-format-when-setting-style-custom-property/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you assign an invalid custom number format to [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) property, Aspose.Cells will not throw an exception. But if you want Aspose.Cells to check whether the assigned custom number format is valid, please set the [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) property to **true**.

## **Check Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) property. Since we have already set the [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) property to **true**, it throws an exception, e.g., “Invalid number format”. Please read the comments inside the code for more help.

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of the Workbook class
    Workbook book;

    // Setting this property to true will cause Aspose.Cells to throw an exception
    // when an invalid custom number format is assigned to the Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put a number into it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access the cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw an exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

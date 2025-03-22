---
title: Using Built-in Styles with C++
linktitle: Using Built-in Styles
type: docs
weight: 80
url: /cpp/using-built-in-styles/
description: C++ code to use Excel built-in styles with Aspose.Cells for C++ API
keywords: c++ use excel built in styles, c++ programmatically apply styles in workbook, programmatically apply styles in workbook, c++ apply built in styles in excel, c++ apply built in styles in workbook, c++ code apply built in styles in workbook, c++ code apply built in styles in excel workbook
---

{{% alert color="primary" %}}

Aspose.Cells provides a vast collection of re-usable styles to format a cell in a spreadsheet document. We can use built-in styles in our workbook and also create custom styles.

{{% /alert %}}

## **How to use Built-in Styles**

The method [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) and the enumeration [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) make it convenient to use built-in styles. Here is a list of all possible built-in styles:

- TWENTY_PERCENT_ACCENT_1
- TWENTY_PERCENT_ACCENT_2
- TWENTY_PERCENT_ACCENT_3
- TWENTY_PERCENT_ACCENT_4
- TWENTY_PERCENT_ACCENT_5
- TWENTY_PERCENT_ACCENT_6
- FORTY_PERCENT_ACCENT_1
- FORTY_PERCENT_ACCENT_2
- FORTY_PERCENT_ACCENT_3
- FORTY_PERCENT_ACCENT_4
- FORTY_PERCENT_ACCENT_5
- FORTY_PERCENT_ACCENT_6
- SIXTY_PERCENT_ACCENT_1
- SIXTY_PERCENT_ACCENT_2
- SIXTY_PERCENT_ACCENT_3
- SIXTY_PERCENT_ACCENT_4
- SIXTY_PERCENT_ACCENT_5
- SIXTY_PERCENT_ACCENT_6
- ACCENT_1
- ACCENT_2
- ACCENT_3
- ACCENT_4
- ACCENT_5
- ACCENT_6
- BAD
- CALCULATION
- CHECK_CELL
- COMMA
- COMMA_1
- CURRENCY
- CURRENCY_1
- EXPLANATORY_TEXT
- GOOD
- HEADER_1
- HEADER_2
- HEADER_3
- HEADER_4
- HYPERLINK
- FOLLOWED_HYPERLINK
- INPUT
- LINKED_CELL
- NEUTRAL
- NORMAL
- NOTE
- OUTPUT
- PERCENT
- TITLE
- TOTAL
- WARNING_TEXT
- ROW_LEVEL
- COLUMN_LEVEL

## C++ code to use built-in styles

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
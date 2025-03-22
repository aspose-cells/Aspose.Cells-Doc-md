---
title: Extract Theme Data from Excel File with C++
linktitle: Extract Theme Data from Excel File
description: Aspose.Cells is a C++ library for working with spreadsheet files. It supports extracting theme data from Excel files, allowing users to obtain the style and formatting information of documents. This article will introduce how to extract theme data from Excel files using the Aspose.Cells library.
keywords: Aspose.Cells, Excel File, Theme Data, Style, Format
type: docs
weight: 120
url: /cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells allows users to extract theme-related data from an Excel file. For example, you can extract the theme name applied to the workbook and the theme color applied to a cell or the borders of the cell, etc.

You can apply a theme to your workbook using Microsoft Excel via Page Layout > Themes command.

{{% /alert %}}

## C++ code to extract theme data from Excel file

The following sample code extracts the theme name applied to the source workbook and then extracts the theme color applied to cell A1 and the theme color applied to the bottom border of the cell.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
---
title: Specifying DBNum Custom Pattern Formatting with C++
linktitle: Specifying DBNum Custom Pattern Formatting
description: Aspose.Cells is a C++ library for working with spreadsheet files that supports formatting dates and numbers using custom formatting patterns. This article will show you how to use the Aspose.Cells library to specify the 'dbnum' custom format pattern so that users have more control over how numbers are displayed.
keywords: Aspose.Cells, C++ library, electronic spreadsheet, custom format pattern, formatting, 'dbnum', control display
type: docs
weight: 110
url: /cpp/specifying-dbnum-custom-pattern-formatting/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells supports the *DBNum* custom pattern formatting. For example, if your cell value is 123 and you specify its custom formatting as [DBNum2][$-804]General then it will be displayed like 壹佰贰拾叁. You can specify your custom formatting of the cell using [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) method and [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) property.

## **Sample Code**

The following sample code illustrates how to specify *DBNum* custom pattern formatting. Please check its [output PDF](43352081.pdf) for more help.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

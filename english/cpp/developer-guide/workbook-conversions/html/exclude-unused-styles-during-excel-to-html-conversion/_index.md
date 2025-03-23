---
title: Exclude Unused Styles during Excel to HTML conversion with C++
linktitle: Exclude Unused Styles
type: docs
weight: 30
url: /cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Learn how to exclude unused styles during Excel to HTML conversion using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Microsoft Excel files may contain many unused styles. When you export the Excel file to HTML format, these unused styles are also exported, which can increase the size of the HTML. You can exclude the unused styles during the conversion of an Excel file to HTML using the [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) property. When you set it to **true**, all unused styles are excluded from the output HTML. The following screenshot displays a sample unused style inside the output HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclude Unused Styles during Excel to HTML conversion**

The following sample code creates a workbook and also creates an unused named style. Since the [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) is set to **true**, this unused named style will not be exported to the [output HTML](61767778.zip). However, if you set it to **false**, then this unused style will be present inside the output HTML, which you can then see in the HTML markup as shown in the above screenshot.

## **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create an unused named style
    Style unusedStyle = wb.CreateStyle();
    unusedStyle.SetName(u"UnusedStyle_XXXXXXXXXXXXXX");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some value in cell C7
    ws.GetCells().Get(u"C7").PutValue(u"This is sample text.");

    // Specify html save options, we want to exclude unused styles
    HtmlSaveOptions opts;

    // Comment this line to include unused styles
    opts.SetExcludeUnusedStyles(true);

    // Save the workbook in html format
    wb.Save(u"outputExcludeUnusedStylesInExcelToHTML.html", opts);

    std::cout << "Workbook saved successfully with unused styles excluded!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
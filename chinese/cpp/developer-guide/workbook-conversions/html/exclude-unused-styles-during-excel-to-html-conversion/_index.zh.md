---
title: 在Excel转HTML时排除未使用的样式，支持C++
linktitle: 排除未使用的样式
type: docs
weight: 30
url: /zh/cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: 学习在使用Aspose.Cells for C++将Excel转换为HTML时排除未使用样式的方法。
---

## **可能的使用场景**

Microsoft Excel文件可能包含许多未使用的样式。在导出为HTML格式时，这些未使用的样式也会被导出，从而增加HTML文件的大小。你可以在将Excel文件转换为HTML时使用[**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/)属性排除未使用的样式。当将其设置为**true**时，所有未使用的样式都将从输出HTML中排除。以下截图显示了输出HTML中的一个未使用样式示例。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **在将 Excel 转换为 HTML 时排除未使用的样式**

以下示例代码创建了一个工作簿，并创建了一个未使用的命名样式。因为[**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/)设置为**true**，这个未使用的命名样式不会导出到[输出HTML](61767778.zip)。但如果你将其设置为**false**，那么这个未用样式将出现在输出HTML中，你可以在HTML标记中看到它，如上方截图所示。

## **示例代码**

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
{{< app/cells/assistant language="cpp" >}}

---
title: 使用C++将Excel导出到带有网格线的HTML
linktitle: 将Excel导出为带有网格线的HTML
type: docs
weight: 40
url: /zh/cpp/export-excel-to-html-with-gridlines/
description: 学习如何使用编号Aspose.Cells for C++导出带网格线的Excel文件到HTML。
---

{{% alert color="primary" %}} 

如果希望导出带有网格线的Excel文件到HTML，请使用【HtmlSaveOptions.GetExportGridLines()】属性，并将其设置为**true**。

{{% /alert %}} 

## **将Excel导出为带有网格线的HTML**
以下示例代码创建一个工作簿并在其工作表填充一些值，然后将其以HTML格式保存，同时将【HtmlSaveOptions.GetExportGridLines()】设置为**true**。

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

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Fill worksheet with some integer values
    for (int r = 0; r < 10; r++)
    {
        for (int c = 0; c < 10; c++)
        {
            ws.GetCells().Get(r, c).PutValue(r * 1);
        }
    }

    // Save workbook in HTML format and export gridlines
    HtmlSaveOptions opts;
    opts.SetExportGridLines(true);
    wb.Save(outDir + u"ExportToHTMLWithGridLines_out.html", opts);

    std::cout << "Workbook exported to HTML with gridlines successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

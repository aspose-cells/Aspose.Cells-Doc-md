---
title: 使用C++将打印区域范围导出为HTML
linktitle: 导出打印区域范围到HTML
type: docs
weight: 60
url: /zh/cpp/export-print-area-range-to/
description: 学习如何使用编号Aspose.Cells for C++将打印区域范围导出到HTML。
---

## **可能的使用场景**

这是一个常见场景，我们只需导出打印区域，即所选范围的单元格，而非整个工作表到HTML中。此功能已在PDF渲染中实现，现在也可以用于HTML。首先，在工作表的页面设置对象中设置打印区域。之后，使用[**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/)标志只导出选中的范围。

## **示例代码**

以下示例代码加载工作簿，然后导出其打印区域到HTML。测试此功能的示例文件可以从以下链接下载：

[sampleInlineCharts.xlsx](79527946.xlsx)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

---
title: 使用C++在加载工作簿时自动调整列宽和行高以适应HTML内容
linktitle: 在加载 HTML 到工作簿时自动调整列和行
type: docs
weight: 120
url: /zh/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: 学习如何在使用Aspose.Cells for C++加载HTML时，将列和行自动调整以适应内容。
---

## **可能的使用场景**

在加载 HTML 文件到 Workbook 对象内部时，您可以同时调整列和行的大小。请将 [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) 属性设置为 **true** 以实现此目的。

## **加载HTML至工作簿时自适应调整列和行**

以下示例代码首先无需加载选项将样本 HTML 加载到 Workbook 中并以 XLSX 格式保存。然后再次加载样本 HTML 到 Workbook 中，但这次在设置 [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) 属性为 **true** 后加载，并以 XLSX 格式保存。请下载两个输出的 Excel 文件，即 [未自动调整列和行的输出 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx) 和 [已自动调整列和行的输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx)。以下截图展示了 [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) 属性对两个输出 Excel 文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

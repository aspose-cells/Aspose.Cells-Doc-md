---
title: 使用C++将Excel转换为带提示的HTML
linktitle: 将 Excel 转换为带有工具提示的 HTML
type: docs
weight: 200
url: /zh/cpp/convert-excel-to-html-with-tooltip/
description: 使用Aspose.Cells在C++中将Excel转换为HTML同时添加提示信息。
---

## **将 Excel 转换为带有工具提示的 HTML**

 有时生成的HTML中文本会被截断，你希望在悬停事件中显示完整的文本作为提示。Aspose.Cells支持这一点，提供了[**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/)属性。将[**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/)属性设置为**true**将会在生成的HTML中添加完整文本作为提示。

以下图片显示了生成的 HTML 文件中的工具提示。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载[源Excel文件](98107416.xlsx)并生成带有提示的[输出HTML文件](98107417.zip)。

示例代码

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

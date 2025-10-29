---
title: 使用C++导出Web浏览器不支持的类似边框样式
linktitle: 在Web浏览器不支持边框样式时导出类似的边框样式
type: docs
weight: 70
url: /zh/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: 学习如何使用Aspose.Cells结合C++导出Web浏览器不支持的边框样式。
---

## **可能的使用场景**

微软Excel支持一些虚线边框类型，但Web浏览器不支持。当你用Aspose.Cells将此类Excel文件转为HTML时，这些边框会被移除。除了移除，Aspose.Cells还支持显示这些边框，通过设置[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)属性为**true**，支持显示未支持的边框，导出到HTML。

## **在Web浏览器不支持边框样式时导出相似的边框样式**

以下示例加载了包含一些不支持边框的【示例Excel文件】(64716806.xlsx)，调用效果如截图所示。截图进一步展示了[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)属性在【输出HTML】(64716804.zip)中的效果。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

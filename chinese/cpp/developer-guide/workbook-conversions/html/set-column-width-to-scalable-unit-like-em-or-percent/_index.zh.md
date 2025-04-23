---
title: 设置列宽为可缩放单位，如em或百分比，使用C++实现
linktitle: 将列宽设置为可伸缩单位，如em或百分比
type: docs
weight: 130
url: /zh/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: 学习如何使用Aspose.Cells for C++将列宽设置为可缩放单位，如em或百分比。
---

从电子表格生成HTML文件非常常见. 列的大小以"pt"为单位定义在许多情况下有效. 但是, 也可能存在不需要固定大小的情况. 例如,如果在显示HTML页面的容器面板宽度为600px, 则如果生成的表格宽度更宽,可能会出现水平滚动条. 在这种情况下, 可以将此固定大小改为em或百分比等可扩展的单位以获得更好的呈现效果. 下面的示例代码可以使用其中的[**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/)设置为**true**来创建可扩展宽度.

可从以下链接下载示例源文件和输出文件：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```c++
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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

---
title: 用C++生成工作表缩略图
linktitle: 生成工作表的缩略图
type: docs
weight: 110
url: /zh/cpp/generate-thumbnail-of-the-worksheet/
description: 使用Aspose.Cells for C++生成Excel工作表的缩略图作为图像。
---

{{% alert color="primary" %}} 

从工作表生成缩略图可能很有用。缩略图是一个小图像，可以粘贴到 Word 文档或 PowerPoint 演示文稿中，以预览工作表内容。它可以添加到网页，用于提供下载原始文档的链接，并且具有各种其他用途。

{{% /alert %}} 

Aspose.Cells for C++允许你将工作表输出为图像文件，从而简化缩略图生成。以下示例代码演示如何使用C++输出工作表到图像文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

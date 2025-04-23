---
title: 使用C++结合ImageOrPrint选项从工作表中提取图像
linktitle: 从工作表中提取图像
type: docs
weight: 140
url: /zh/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: 学习如何使用Aspose.Cells for C++从Excel工作表中提取图片并保存到本地驱动器。
---

{{% alert color="primary" %}} 

Microsoft Excel 用户可以将图像添加到电子表格中。通过 Aspose.Cells，可以读取 Microsoft Excel 文件中的图像并将其保存到本地驱动器。本文显示了如何实现。

{{% /alert %}} 

下面的示例代码显示了如何从 Excel 文件中提取图像并保存。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

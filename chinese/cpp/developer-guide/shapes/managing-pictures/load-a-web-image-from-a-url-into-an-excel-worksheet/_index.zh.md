---
title: 从URL加载网页图片到Excel工作表（C++）
linktitle: 将网络图片从URL加载到Excel工作表
type: docs
weight: 30
url: /zh/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: 了解如何使用C++和Aspose.Cells for C++ API将URL中的图片转换为Excel嵌入图片。
keywords: Excel显示URL图片，Excel URL转图片，在Excel中显示来自URL的图片，Excel插入来自URL的图片，转换URL到Excel中的图片，Excel中的URL图片，从URL加载图片到Excel，C++，Excel
---

## 从URL加载图像到Excel工作表

Aspose.Cells for C++ API 提供了一种直接从URL加载图片到Excel工作表的方法。本文介绍如何将图片数据下载到内存流中，并使用Aspose.Cells将其插入到工作表中。图片会嵌入到Excel文件中，打开时无需外部下载。

## 示例代码

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

对于需要始终从URL更新图片的场景，使用[从网页地址插入链接图片](/cells/zh/cpp/insert-a-linked-picture-from-web-address/)中描述的方法。此方法每次打开工作表时都从URL加载图片。

{{% /alert %}}

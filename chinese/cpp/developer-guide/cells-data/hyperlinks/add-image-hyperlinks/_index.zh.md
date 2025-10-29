---
title: 使用C++添加超链接图片
linktitle: 添加图像超链接
type: docs
weight: 140
url: /zh/cpp/add-image-hyperlinks/
description: 通过Aspose.Cells for C++ API学习如何添加图片超链接。
keywords: 添加图像超链接，插入图像超链接
---

{{% alert color="primary" %}} 

超链接对于访问其他工作表或网站上的信息非常有用。Microsoft Excel允许用户在单元格中的文本和图像上添加超链接。图像超链接可以使工作表的导航更加方便，例如作为下一个和上一个按钮，或者链接到特定网站的标志。本文档说明了如何使用Aspose.Cells在工作表中插入图像超链接。

{{% /alert %}} 

Aspose.Cells允许您在运行时向电子表格中的图像添加超链接。可以设置和修改链接的屏幕提示和地址。以下示例代码说明了如何向工作表中添加图像超链接。

```c++
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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

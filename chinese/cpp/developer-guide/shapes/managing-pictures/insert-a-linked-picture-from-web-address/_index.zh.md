---
title: 从Web地址插入链接图片（C++）
linktitle: 从Web地址插入链接图片
type: docs
weight: 450
url: /zh/cpp/insert-a-linked-picture-from-web-address/
description: 学习如何使用Aspose.Cells for C++从Web地址在工作表中插入链接图片。
---

{{% alert color="primary" %}}

有时您需要从Web（http://）将图片插入工作表中。为此，指定图片的URL，每次在Microsoft Excel中打开电子表格时都会下载图片。该图像并没有实际嵌入到Excel文档中，而是指向Web资源。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中（例如2007）：

1. 单击**插入**菜单，然后选择**图片**。
1. 在插入图片对话框中指定图片的Web地址。

## **使用Aspose.Cells for C++**

Aspose.Cells for C++支持使用[**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/)方法添加链接图片。该方法返回一个[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)对象。

以下示例展示了如何将来自Web地址的链接图片添加到工作表中。

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

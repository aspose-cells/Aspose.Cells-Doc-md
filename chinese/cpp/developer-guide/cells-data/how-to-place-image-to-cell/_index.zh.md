---
title: 如何使用C++在单元格中插入图片
linktitle: 如何在单元格中插入图片
type: docs
weight: 130
url: /zh/cpp/how-to-insert-picture-in-cell/
description: 学习如何使用C++将图片插入到Aspose.Cells的单元格中。
keywords: 如何在单元格中插入图片，在单元格上插入图片，在单元格中放置图片，在单元格上放置图片，如何在单元格中放置图像，如何在单元格上放置图像，在图片在单元格和在单元格上放置之间切换，从单元格中切换到单元格上放置、从单元格中切换到单元格上放置。
---

## **可能的使用场景**
图片为您的工作表增添一抹亮色，提供内容的直观表现，也使您更容易理解数据并获得洞察。尽管多年来您一直可以在Excel中使用图片，但Excel最近才启用了图片成为实际单元格值的功能。即使布局被修改，图片仍将与数据绑定。您可以在表格中使用它，排序、筛选、包含在公式中等等！

## **如何使用Excel在单元格中插入图片**
关于如何在Excel中在单元格中插入图片，请按照以下步骤操作：

1. 转到“插入”选项卡，单击“图片”选项。
2. 选择**放入单元格**。 从“从下拉菜单中插入图片”中选择以下来源之一（**此设备**，**库存图片** 和 **在线图片**）。 此设备用于从设备中插入图片。 库存图片用于从库存图片中插入图片。 在线图片用于从网络中插入图片。
<br>
<img src="1.png" width=60% />
3. 选择图片并将其插入到单元格中。
<br>
<img src="8.png" width=60% />

## **如何在Excel中在单元格上放置图片**
关于如何在Excel中在单元格上放置图片，请按照以下步骤操作：

1. 转到“插入”选项卡，单击“图片”选项。
2. 选择**放在单元格上**。 从“从下拉菜单中插入图片”中选择以下来源之一（**此设备**，**库存图片** 和 **在线图片**）。 此设备用于从设备中插入图片。 库存图片用于从库存图片中插入图片。 在线图片用于从网络中插入图片。
<br>
<img src="2.png" width=60% />
3. 选择图片并在单元格上插入图片。
<br>
<img src="3.png" width=60% />

## **如何在Excel中从单元格中的图片切换到单元格上的图片**
您可以轻松地从**单元格中**切换到**单元格上**。 请按照以下步骤操作：
1. 右键单元格，选择**单元格中** > **放在单元格上**。 
<br>
<img src="4.png" width=60% />
2. 切换后的结果如下：
<br>
<img src="5.png" width=60% />

## **如何在Excel中从单元格上方的图片切换到单元格内的图片**
您可以轻松地从 **单元格上方的图片** 切换到 **单元格内的图片**。请按照以下步骤操作：
1. 右键单击图片，然后选择 **放置在单元格中**。 
<br>
<img src="6.png" width=60% />
2. 切换后的结果如下：
<br>
<img src="7.png" width=60% />

## **使用C++插入图片到单元格的方法**
使用 Aspose.Cells 在单元格中插入图片。请参阅以下示例代码。执行示例代码后，将在单元格中插入一张图片。
1. 实例化一个Workbook对象。 
2. 获取要插入图片的单元格。
3. 设置Cell.EmbeddedImage属性。 
4. 最后，以[out.xlsx]格式保存工作簿。 

## **示例代码**

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cell D8
    Cell d8 = worksheet.GetCells().Get(u"D8");

    // Read image file into byte vector
    std::ifstream file("aspose.png", std::ios::binary);
    std::vector<uint8_t> imageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // Convert to Aspose's Vector and set embedded image in cell D8
    d8.SetEmbeddedImage(Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}

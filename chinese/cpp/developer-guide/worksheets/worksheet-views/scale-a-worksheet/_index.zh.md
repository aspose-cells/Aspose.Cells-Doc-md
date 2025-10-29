---
title: 如何用 C++ 缩放工作表
linktitle: 如何缩放工作表
type: docs
weight: 130
url: /zh/cpp/how-to-scale-a-worksheet/
description: 本文将说明如何用 Aspose.Cells 库及 C++ 代码缩放工作表。
keywords: C++ 缩放工作表，如何用 C++ 缩放工作表，在 C++ 中缩放工作表。
---

## **可能的使用场景**
缩放工作表在不同场景下可能具备不同用途，以下是一些常见的原因：
1. 适应页面：确保所有内容在打印时适合单页或特定页数，更易于阅读和管理，无需翻页。

1. 演示：让工作表看起来更有条理和专业，特别是在会议或报告中与他人分享时。

1. 可读性：调整文本和其他元素的大小以提高可读性，尤其适用于阅读较小字体有困难的人群。

1. 空间管理：优化工作表的空间利用，确保没有不必要的空白区域，所有重要信息都能在不需要大量滚动的情况下显示。

1. 数据可视化：在图表和图形中，缩放可以帮助更易于理解，通过调整大小以适应可用空间。

1. 一致性：在多个工作表或文档中保持一致的外观和感觉，在专业和教育环境中特别重要。

## **如何在Excel中缩放工作表**
在Excel中缩放工作表可以帮助你在打印时将内容适配到一页或指定的页数。以下是缩放工作表的步骤：

1. 打开你的工作表：打开你想要缩放的Excel工作表。

1. 转到页面布局标签：在功能区中点击“页面布局”标签。

1. “缩放以适应”组：在“页面布局”标签中，找到“缩放以适应”组。这里有调整缩放的选项。宽度：允许你设置打印工作表的宽页数。高度：允许你设置打印工作表的高页数。缩放：你也可以在这里设置自定义的缩放百分比。
<br>
<img src="1.png" width=60% />

1. 调整宽度和高度：设置为你需要的页数。例如，如果希望工作表在一页内显示，将两者都设置为1页。

1. 调整缩放百分比（如果需要）：如果偏好用具体的缩放百分比，可以调整“缩放”框。例如，将其设置为50%，将使内容变为原来的一半大小。


## **如何使用C++缩放工作表**
Aspose.Cells是一个强大的库，用于以编程方式操作Excel文件。要使用Aspose.Cells缩放工作表，需要按照以下步骤：加载[示例文件](sample.xlsx)并调整打印设置，使内容适合所需的页数或特定的百分比大小。

### **示例：适合一页**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the worksheet to fit to 1 page wide and 1 page tall
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the modified workbook
    workbook.Save(u"output_fit_to_page.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
<br>
<img src="3.png" width=60% />

### **示例：按百分比缩放**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the scaling to a specific percentage (e.g., 75%)
    pageSetup.SetZoom(75);

    // Save the modified workbook
    workbook.Save(u"output_scaled_percentage.xlsx");

    // Clean up Aspose.Cells resources
    Aspose::Cells::Cleanup();

    return 0;
}
```
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="cpp" >}}

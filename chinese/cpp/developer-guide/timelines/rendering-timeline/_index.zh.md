---
title: 用C++绘制时间线
type: docs
weight: 40
url: /zh/cpp/rendering-timeline/
description: 在C++中使用Aspose.Cells管理Excel文件的时间线。
keywords: 在没有Office 2013、Office 2016、Office 2019和Office 365的情况下渲染时间轴
---

## **可能的使用场景**
Aspose.Cells支持在不使用office 2013、office 2016、office 2019和office 365的情况下呈现时间轴形状。如果将工作表转换为图像，或者将工作簿保存为PDF或HTML格式，就会看到时间轴已正确呈现。

## **呈现时间轴**
以下示例代码加载包含现有时间轴的[sample Excel file](input.xlsx)，根据时间轴名称获取形状对象，然后通过Shape.ToImage()方法将其呈现为图片。以下图片是[output image](out.png)，显示了已呈现的时间轴。正如你所见，时间轴已正确呈现，并且看起来与示例Excel文件中的相同。

![todo:image_alt_text](out.png)
### **示例代码**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

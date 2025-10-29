---
title: 用C++插入时间线
linktitle: 时间轴
type: docs
weight: 170
url: /zh/cpp/create-timeline/
description: 学习如何用C++和Aspose.Cells创建时间线。
---

## **可能的使用场景**

不必调整筛选器显示日期，您可以使用数据透视表时间线——一种动态筛选选项，让您轻松按日期/时间筛选，并通过滑块控制放大所需时间段。Microsoft Excel允许通过选择数据透视表并点击*插入 > 时间线*来创建时间线。Aspose.Cells也支持使用[**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/)方法创建时间线。

## **创建时间轴到透视表**

请参阅以下示例代码。它加载包含透视表的[示例Excel文件](input.xlsx)，然后根据第一个基本透视字段创建时间轴。最后，它以[output XLSX](output.xlsx)格式保存工作簿。以下截图显示了Aspose.Cells在输出Excel文件中创建的时间轴。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}

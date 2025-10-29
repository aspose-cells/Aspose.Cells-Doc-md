---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/nodejs-cpp/create-timeline/
description: 学习如何使用Aspose.Cells for Node.js via C++创建时间线。
---

## **可能的使用场景**

你可以使用数据透视表时间线——一种动态筛选选项，轻松按日期/时间筛选，并用滑块控制放大你想要的时间段。微软Excel允许你通过选择数据透视表然后点击*插入>时间线*来创建时间线。Aspose.Cells for Node.js via C++还允许你使用[**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-)方法创建时间线。

## **创建时间轴到透视表**

请查看以下示例代码。它加载包含数据透视表的[示例Excel文件](input.xlsx)。然后根据第一个基础数据透视字段创建时间线。最后，将工作簿保存为[输出XLSX](output.xlsx)。下方截图显示了由Aspose.Cells for Node.js via C++在输出Excel文件中创建的时间线。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}

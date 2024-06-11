---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/net/create-timeline/
description: 学习如何使用Aspose.Cells创建时间轴。
---

## **可能的使用场景**

与调整筛选器以显示日期不同，您可以使用透视表时间轴——一种动态筛选器选项，它可让您轻松按日期/时间进行筛选，并使用滑块控件放大您想要的时间段。Microsoft Excel允许您通过选择一个透视表然后单击*插入 > 时间轴*来创建时间轴。Aspose.Cells还允许您使用[**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index)方法创建时间轴。

## **创建时间轴到透视表**

请参阅以下示例代码。它加载包含透视表的[示例Excel文件](input.xlsx)，然后根据第一个基本透视字段创建时间轴。最后，它以[output XLSX](output.xlsx)格式保存工作簿。以下截图显示了Aspose.Cells在输出Excel文件中创建的时间轴。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}


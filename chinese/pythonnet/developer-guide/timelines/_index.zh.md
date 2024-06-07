---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/python-net/create-timeline/
description: 学习如何在Python中通过.NET使用Aspose.Cells创建时间轴。
keywords: Aspose.Cells for Python Excel，Excel Python库，Python在Excel中无需创建时间轴，通过Aspose.Cells for Python添加时间轴，在Aspose.Cells for Python中使用插入时间轴。
---

## **可能的使用场景**

你可以使用数据透视表时间轴来代替调整过滤器显示日期，时间轴是一个动态筛选选项，让你可以通过一个滑块轻松筛选日期/时间，并放大你所需要的时段。Microsoft Excel允许你通过选择一个数据透视表然后单击*插入 > 时间轴*来创建时间轴。Aspose.Cells for Python通过.NET也允许你使用[**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)方法创建时间轴。

## **使用Aspose.Cells for Python Excel库为数据透视表创建时间轴的方法**

请参阅以下示例代码。它加载包含数据透视表的[示例Excel文件](input.xlsx)。然后根据第一个基本数据透视字段创建时间轴。最后，将工作簿以[输出XLSX](output.xlsx)格式保存。以下屏幕截图显示了Aspose.Cells for Python通过.NET在输出Excel文件中创建的时间轴。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}


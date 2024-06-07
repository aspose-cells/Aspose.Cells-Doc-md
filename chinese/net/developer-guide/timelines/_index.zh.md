---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/net/create-timeline/
description: 学习如何使用Aspose.Cells创建时间轴。
---

## **可能的使用场景**

您可以使用PivotTable时段，而不是调整筛选器来显示日期——这是一种动态筛选选项，让您可以轻松按日期/时间进行筛选，并使用滑块控件放大所需的期间。Microsoft Excel允许您通过选择一个数据透视表，然后点击*插入 > 时间轴*来创建时间轴。Aspose.Cells也允许您使用[**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index)方法创建时间轴。

## **创建时间轴到数据透视表**

请查看以下示例代码。它加载包含数据透视表的[示例Excel文件](input.xlsx)。然后基于第一个基本数据透视表字段创建时间轴。最后，将工作簿保存为[output XLSX](output.xlsx)格式。以下截图显示了Aspose.Cells在输出Excel文件中创建的时间轴。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}


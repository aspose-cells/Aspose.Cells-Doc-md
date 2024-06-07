---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/java/create-timeline/
description: 学习如何使用Aspose.Cells for Java创建时间轴。
---

## **可能的使用场景**

您可以使用PivotTable Timeline而不是调整筛选器来显示日期——这是一种动态过滤器选项，可让您轻松按日期/时间进行筛选，并使用滑块控件放大您想要的时间段。 Microsoft Excel允许您通过选择数据透视表，然后单击*插入>时间轴*来创建时间轴。 Aspose.Cells for Java还允许您使用[**Worksheet.getTimelines.add()**]方法创建时间轴。

## **创建时间轴到数据透视表**

请查看以下示例代码。它加载包含数据透视表的[示例Excel文件](input.xlsx)。然后基于第一个基本数据透视表字段创建时间轴。最后，将工作簿保存为[output XLSX](output.xlsx)格式。以下截图显示了Aspose.Cells在输出Excel文件中创建的时间轴。

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}


---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/java/create-timeline/
description: 学习如何使用Aspose.Cells For java创建时间轴。
---

## **可能的使用场景**

您可以使用数据透视表时间轴动态筛选选项，而不是调整筛选器来显示日期，轻松筛选日期/时间，并使用滑块控件放大您想要的时段。Microsoft Excel允许您通过选择一个数据透视表，然后单击*插入 > 时间轴* 来创建时间轴。Aspose.Cells for java也允许您使用[**Worksheet.getTimelines.add()**]方法创建时间轴。

## **创建时间轴到透视表**

请参阅以下示例代码。它加载包含透视表的[示例Excel文件](input.xlsx)，然后根据第一个基本透视字段创建时间轴。最后，它以[output XLSX](output.xlsx)格式保存工作簿。以下截图显示了Aspose.Cells在输出Excel文件中创建的时间轴。

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

{{< app/cells/assistant language="java" >}}

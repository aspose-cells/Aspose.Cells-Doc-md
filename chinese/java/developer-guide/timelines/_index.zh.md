---
title: 插入时间线
linktitle: 时间线
type: docs
weight: 170
url: /zh/java/create-timeline/
description: 了解如何使用 Aspose.Cells For java 创建时间线。
---
## **可能的使用场景**

您可以使用数据透视表时间轴而不是调整过滤器来显示日期——这是一种动态过滤器选项，可让您轻松按日期/时间进行过滤，并使用滑块控件放大您想要的时间段。 Microsoft Excel 允许您通过选择数据透视表然后单击*插入 > 时间线*Aspose.Cells for java 还允许您使用 [**Worksheet.getTimelines.add()**] 方法创建时间线。

## **为数据透视表创建时间线**

请参阅以下示例代码。它加载了[示例 Excel 文件](input.xlsx)包含数据透视表。然后它根据第一个基本数据透视字段创建时间线。最后，它将工作簿保存在[输出 XLSX](output.xlsx)格式。以下屏幕截图显示了 Aspose.Cells 在输出 Excel 文件中创建的时间线。

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}


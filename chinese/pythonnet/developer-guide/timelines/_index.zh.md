---
title: 插入时间轴
linktitle: 时间线
type: docs
weight: 170
url: /zh/python-net/create-timeline/
description: 了解如何使用 Aspose.Cells for Python via .NET 创建时间线。
---
##  **可能的使用场景**

您可以使用数据透视表时间线，而不是调整过滤器来显示日期，这是一种动态过滤器选项，可让您轻松地按日期/时间进行过滤，并使用滑块控件放大所需的时间段。 Microsoft Excel 允许您通过选择数据透视表然后单击*插入 > 时间线*来创建时间线。 Aspose.Cells for Python via .NET 还允许您使用创建时间线[**工作表.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)方法。

##  **创建数据透视表的时间线**

请参阅以下示例代码。它加载了[Excel 文件示例](input.xlsx)包含数据透视表。然后，它根据第一个基本枢轴字段创建时间线。最后，它将工作簿保存在[输出XLSX](output.xlsx)格式。以下屏幕截图显示了输出 Excel 文件中 Aspose.Cells for Python via .NET 创建的时间线。

![待办事项：图像_替代_文本](create-timeline-to-a-pivot-table_1.png)

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}


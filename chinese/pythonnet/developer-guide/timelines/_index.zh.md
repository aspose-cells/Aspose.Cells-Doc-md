---
title: 插入时间轴
linktitle: 时间轴
type: docs
weight: 170
url: /zh/python-net/create-timeline/
description: 学习如何使用 Aspose.Cells for Python via .NET 创建时间轴。
keywords: Aspose.Cells for Python Excel、Excel Python 库、Python 在 Excel 中创建时间轴、使用 Aspose.Cells for Python 添加时间轴、使用 Aspose.Cells for Python 插入时间轴。
---

## **可能的使用场景**

您可以使用数据透视表时间轴，而不是调整筛选器以显示日期，这是一个动态筛选选项，可让您轻松按日期/时间进行筛选，并使用滑块控件放大所需的时间段。微软 Excel 允许您通过选择数据透视表然后单击 *插入 > 时间轴* 来创建时间轴。Aspose.Cells for Python via .NET 也允许您使用 [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods) 方法创建时间轴。

## **如何使用 Aspose.Cells for Python Excel 库向数据透视表创建时间轴**

请参阅以下示例代码。它加载包含数据透视表的 [示例 Excel 文件](input.xlsx)，然后基于第一个基本数据透视字段创建时间轴。最后，它将工作簿保存为 [output XLSX](output.xlsx) 格式。以下截图展示了 Aspose.Cells for Python via .NET 在输出的 Excel 文件中创建的时间轴。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}


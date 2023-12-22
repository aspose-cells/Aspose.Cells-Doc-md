---
title: 插入切片机
linktitle: 切片机
type: docs
weight: 170
url: /zh/python-net/create-slicer/
description: 使用 Aspose.Cells 管理 Excel 文件的切片器。
---
##  **可能的使用场景**

切片器用于快速过滤数据。它可用于过滤表或数据透视表中的数据。 Microsoft Excel 允许您通过选择表或数据透视表然后单击*插入 > 切片器*来创建切片器。 Aspose.Cells for Python via .NET 还允许您使用以下命令创建切片器[**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField)方法。

##  **创建数据透视表的切片器**

请参阅以下示例代码。它加载了[Excel 文件示例](67338470.xlsx)包含数据透视表。然后，它根据第一个基本枢轴字段创建切片器。最后，它将工作簿保存在[输出XLSX](67338471.xlsx)和[输出XLSB](67338472.xlsb)格式。以下屏幕截图显示了输出 Excel 文件中由 Aspose.Cells 创建的切片器。

![待办事项：图像_替代_文本](create-slicer-to-a-pivot-table_1.png)

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

##  **创建切片器到 Excel 表**

请参阅以下示例代码。它加载了[Excel 文件示例](sampleCreateSlicerToExcelTable.xlsx)其中包含一个表。然后它根据第一列创建切片器。最后，它将工作簿保存在[输出XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

##  **高级主题**
- [更改切片器属性](/cells/zh/python-net/change-slicer-properties/)
- [在将 Excel 渲染为 PDF 时绘制切片器](/cells/zh/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [格式化切片器](/cells/zh/python-net/formatting-slicer/)
- [拆除切片机](/cells/zh/python-net/removing-slicer/)
- [渲染切片器](/cells/zh/python-net/rendering-slicer/)
- [更新切片器](/cells/zh/python-net/updating-slicer/)

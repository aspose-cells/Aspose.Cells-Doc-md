---
title: 插入切片器
linktitle: 切片器
type: docs
weight: 170
url: /zh/python-net/create-slicer/
description: 使用Aspose.Cells管理Excel文件的切片器。
keywords: 使用 Aspose.Cells for Python Excel、Excel Python 库，在不使用 Excel 的情况下创建切片器，通过 Aspose.Cells for Python 添加切片器，使用 Aspose.Cells for Python 插入切片器。
---

## **可能的使用场景**

切片器用于快速过滤数据。它既可以用于表格，还可以用于数据透视表中的数据过滤。Microsoft Excel 允许您通过选择表格或数据透视表，然后单击 *“插入 > 切片器”* 来创建切片器。Aspose.Cells for Python via .NET 也允许您使用该 [**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField) 方法来创建切片器。

## **如何使用 Aspose.Cells for Python Excel 库在数据透视表中创建切片器**

请参阅以下示例代码。它加载包含数据透视表的 [示例 Excel 文件](67338470.xlsx)。然后基于第一个基本数据透视表字段创建切片器。最后，它以 [输出 XLSX](67338471.xlsx) 和 [输出 XLSB](67338472.xlsb) 格式保存工作簿。以下屏幕截图显示了由 Aspose.Cells 在输出 Excel 文件中创建的切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

## **如何使用 Aspose.Cells for Python Excel 库创建 Excel 表格的切片器**

请查看以下示例代码。它加载包含数据表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器。最后，将工作簿保存为[output XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

## **高级主题**
- [更改切片器属性](/cells/zh/python-net/change-slicer-properties/)
- [在将 Excel 渲染为 PDF 时绘制分析器](/cells/zh/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [格式化切片器](/cells/zh/python-net/formatting-slicer/)
- [移除切片器](/cells/zh/python-net/removing-slicer/)
- [呈现切片器](/cells/zh/python-net/rendering-slicer/)
- [更新分析器](/cells/zh/python-net/updating-slicer/)
{{< app/cells/assistant language="python-net" >}}

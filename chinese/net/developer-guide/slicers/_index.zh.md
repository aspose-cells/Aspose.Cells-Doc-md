---
title: 插入切片器
linktitle: 切片器
type: docs
weight: 170
url: /zh/net/create-slicer/
description: 使用Aspose.Cells管理Excel文件的切片器。
---

## **可能的使用场景**

切片器用于快速过滤数据。它可用于在表格或数据透视表中过滤数据。Microsoft Excel允许您通过选择表格或数据透视表，然后单击*插入 > 切片器* 来创建切片器。Aspose.Cells也允许您使用[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index)方法创建切片器。

## **为数据透视表创建切片器**

请参阅以下示例代码。它加载包含数据透视表的 [示例 Excel 文件](67338470.xlsx)。然后基于第一个基本数据透视表字段创建切片器。最后，它以 [输出 XLSX](67338471.xlsx) 和 [输出 XLSB](67338472.xlsb) 格式保存工作簿。以下屏幕截图显示了由 Aspose.Cells 在输出 Excel 文件中创建的切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **为Excel表创建切片器**

请查看以下示例代码。它加载包含数据表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器。最后，将工作簿保存为[output XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **高级主题**
- [更改切片器属性](/cells/zh/net/change-slicer-properties/)
- [在将 Excel 渲染为 PDF 时绘制分析器](/cells/zh/net/draw-slicer-while-rendering-excel-to-pdf/)
- [格式化切片器](/cells/zh/net/formatting-slicer/)
- [移除切片器](/cells/zh/net/removing-slicer/)
- [呈现切片器](/cells/zh/net/rendering-slicer/)
- [更新分析器](/cells/zh/net/updating-slicer/)

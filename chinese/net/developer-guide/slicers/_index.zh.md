---
title: 插入分割器
linktitle: 切片器
type: docs
weight: 170
url: /zh/net/create-slicer/
description: 使用Aspose.Cells管理Excel文件的分割器
---

## **可能的使用场景**

分割器可快速过滤数据。它可用于过滤表格或数据透视表中的数据。Microsoft Excel允许您通过选择表格或数据透视表，然后点击*插入 > 分割器*来创建分割器。Aspose.Cells还允许您使用[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index)方法创建分割器。

## **为数据透视表创建分割器**

请参阅以下示例代码。它加载包含数据透视表的[示例Excel文件](67338470.xlsx)。然后基于第一个基本数据透视字段创建分割器。最后，将工作簿另存为[输出XLSX](67338471.xlsx)和[输出XLSB](67338472.xlsb)格式。以下截图显示了Aspose.Cells在输出Excel文件中创建的分割器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **为Excel表创建分割器**

请参阅以下示例代码。它加载包含表格的[示例Excel文件](sampleCreateSlicerToExcelTable.xlsx)。然后基于第一列创建分割器。最后，将工作簿另存为[输出XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **高级主题**
- [更改分割器属性](/cells/zh/net/change-slicer-properties/)
- [在将Excel渲染为PDF时绘制分割器](/cells/zh/net/draw-slicer-while-rendering-excel-to-pdf/)
- [格式化分割器](/cells/zh/net/formatting-slicer/)
- [移除分割器](/cells/zh/net/removing-slicer/)
- [渲染分割器](/cells/zh/net/rendering-slicer/)
- [更新分割器](/cells/zh/net/updating-slicer/)

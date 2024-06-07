---
title: 将Excel数据导出到DataTable并检查混合数据类型
type: docs
weight: 280
url: /zh/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: 通过Aspose.Cells for .NET API学习如何将Excel数据导出到DataTable并检查混合数据类型。
keywords: 将Excel数据导出到DataTable并检查混合数据类型，将工作簿数据导出到DataTable并检查混合数据类型，将数据导出到DataTable并检查混合数据类型，将工作表数据导出到DataTable并检查混合数据类型。
---

## **可能的使用场景**
如果一列包含各种类型的数据，当将数据导出到DataTable时，程序会抛出一个类型异常。对于默认情况下导出数据表，Aspose.Cells会基于列中的第一个（单元格）值评估值的数据类型。因此，如果该值是数字，则意味着该列的数据类型是数值，这是合理的。如果第一个值是数字，但列中有字母数字数据或值，则应分配字符串数据类型。为了解决这个问题，请使用[ExportDataTable overload](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1)涉及[ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/)并尝试将[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)布尔属性设置为"true"，如果一列既有数值又有字符串值，以避免错误。

## **将Excel数据导出到DataTable并检查混合数据类型**

下面的样本解释了[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)属性的使用，用于将Excel数据导出到数据表。请参阅[示例Excel文件](sample.xlsx)，其中的屏幕截图和控制台输出供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **截图**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **控制台输出**

以下是上述示例代码的控制台调试输出

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}

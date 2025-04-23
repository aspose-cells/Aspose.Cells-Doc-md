---
title: 将Excel数据导出到DataTable中并检查混合数据类型
type: docs
weight: 280
url: /zh/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: 使用Aspose.Cells for .NET API学习如何将Excel数据导出到数据表，并检查混合数据类型。
keywords: 将Excel数据导出到DataTable并检查混合数据类型，将工作簿数据导出到DataTable并检查混合数据类型，将数据导出到DataTable并检查混合数据类型，将工作表数据导出到DataTable并检查混合数据类型。
---

## **可能的使用场景**
如果列包含各种类型的数据，则在将数据导出到DataTable时，程序会抛出类型异常。默认情况下，Aspose.Cells根据列中的第一个（单元格）值评估值的数据类型。因此，如果值是数字，则意味着该列的数据类型将为数字，这是合理的。如果第一个值是数字，但列中有字母数字数据或值，则应分配字符串数据类型。为了解决这个问题，请使用[ExportDataTable overload](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1)，这涉及[ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/)，请尝试将[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)布尔属性设置为"true"，如果一个列同时具有数值和字符串值，可以避免错误。

## **将Excel数据导出到DataTable并检查混合数据类型**

以下示例说明了使用[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)属性将Excel数据导出到数据表。请参考[示例Excel文件](sample.xlsx)，以及其屏幕截图和控制台输出。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **屏幕截图**
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
{{< app/cells/assistant language="csharp" >}}

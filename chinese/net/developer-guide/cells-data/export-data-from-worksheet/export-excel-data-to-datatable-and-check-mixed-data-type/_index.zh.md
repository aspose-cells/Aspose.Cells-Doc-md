---
title: 将 Excel 数据导出到 DataTable 并检查混合数据类型
type: docs
weight: 280
url: /zh/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: 通过 Aspose.Cells for .NET API 了解如何将 Excel 数据导出到 DataTable 并检查混合数据类型。
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **可能的使用场景**
如果某列包含各种类型的数据，则程序在将数据导出到DataTable时会抛出类型异常。对于导出数据表，默认情况下，Aspose.Cells 根据列中的第一个（单元格）值评估值的数据类型。因此，如果值为数字，则意味着该列的数据类型将为数字，这是合理的。如果第一个值是数字，但列中有字母数字数据或值，则应分配字符串数据类型。为了应对它，请使用[导出数据表重载](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1)其中涉及[导出数据表选项](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/)并尝试设置[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)如果列同时具有数字和字符串值以避免错误，则布尔属性设置为“true”。

##  **将 Excel 数据导出到 DataTable 并检查混合数据类型**

下面的示例解释了使用[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)属性将Excel数据导出到数据表。请参阅[Excel 文件示例](sample.xlsx)、其屏幕截图和控制台输出以供参考。

###  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **截屏**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **控制台输出**

以下是上述示例代码的控制台调试输出

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}

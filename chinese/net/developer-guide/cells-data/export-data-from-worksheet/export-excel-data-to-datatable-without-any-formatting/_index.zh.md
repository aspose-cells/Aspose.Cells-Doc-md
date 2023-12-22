---
title: 将 Excel 数据导出到 DataTable，无需任何格式
type: docs
weight: 280
url: /zh/net/export-excel-data-to-datatable-without-any-formatting/
description: 通过 Aspose.Cells for .NET API 了解如何将 Excel 数据导出到数据表而不进行任何格式化。
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---
{{% alert color="primary" %}}

有时用户希望将Excel数据导出到数据表中而不进行任何格式化。例如，如果某个单元格的值为 0.012345，并且其格式设置为显示两位小数，那么当用户将 Excel 数据导出到数据表时，它将导出为 0.01，而不是 0.012345。为了解决这个问题，Aspose.Cells提供了[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)可以采用这三个值之一的属性

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

如果您将其设置为[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)，然后它将不带任何格式地导出数据。

{{% /alert %}}

## 示例代码

下面的示例解释了使用[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)属性来导出带或不带任何格式的 Excel 数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

##  **控制台输出**

以下是上述示例代码的控制台调试输出

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}

---
title: 无任何格式导出Excel数据到DataTable
type: docs
weight: 280
url: /zh/net/export-excel-data-to-datatable-without-any-formatting/
description: 使用Aspose.Cells for .NET API学习如何将Excel数据导出到数据表而不带任何格式。
keywords: 将Excel数据导出到DataTable而不进行任何格式设置，指定单元格值格式策略，在将数据导出到DataTable时添加格式策略。 
---

{{% alert color="primary" %}}

有时用户希望将Excel数据导出到数据表时不进行任何格式设置。例如，如果某个单元格的值为0.012345，并且已格式化为显示两位小数，则当用户将Excel数据导出到数据表时，它将导出为0.01而不是0.012345。为解决这个问题，Aspose.Cells提供了[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)属性，可以取这三个值之一

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

如果将其设置为[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)，则将导出不带任何格式的数据。

{{% /alert %}}

## 示例代码

以下示例说明了使用[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)属性将Excel数据以及不带任何格式的方式导出。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **控制台输出**

以下是上述示例代码的控制台调试输出

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}

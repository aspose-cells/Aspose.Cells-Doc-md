---
title: 将Excel数据导出到DataTable而不使用任何格式
type: docs
weight: 280
url: /zh/net/export-excel-data-to-datatable-without-any-formatting/
description: 通过Aspose.Cells for .NET API学习如何将Excel数据导出到DataTable而不使用任何格式。
keywords: 将Excel数据导出到DataTable而不使用任何格式，指定单元格值格式策略，在导出数据到DataTable时添加格式策略。 
---

{{% alert color="primary" %}}

有时用户希望将Excel数据导出到数据表而不使用任何格式。例如，如果某单元格的值为0.012345，并且格式为显示两位小数，那么当用户将Excel数据导出到数据表时，它将作为0.01导出，而不是0.012345。为解决这个问题，Aspose.Cells提供了[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)属性，它可以取这三个值之一

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

如果将其设置为[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)，则它将以没有任何格式的方式导出数据。

{{% /alert %}}

## 示例代码

以下示例解释了使用[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)属性导出带有或不带任何格式的Excel数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **控制台输出**

以下是上述示例代码的控制台调试输出

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}

---
title: .NET中从工作表导出数据
linktitle: 从工作表导出数据
type: docs
weight: 180
url: /zh/net/export-data-from-worksheet/
description: 本文介绍如何使用C#将工作表中的数据导出或导入到DataTable中。
keywords: C#从工作表导出数据, C#将数据导出到DataTable, 包含强类型数据的列, 包含非强类型数据的列, 使用标志跳过列名的C#导出范围, C#如何导出带有标题的范围。
---

## 概述

本文介绍如何使用C#将工作表数据导出到DataTable。 它涵盖以下主题

_格式_: **Excel**
- [C# Excel到DataTable](#csharp-excel-to-datatable)
- [C#将Excel转换为DataTable](#csharp-convert-excel-to-datatable)
- [C#将Excel导入到DataTable](#csharp-import-excel-to-datatable)
- [从Excel中导出到DataTable的C#](#csharp-export-to-datatable-from-excel)

_格式_: **XLS**
- [C# XLS转DataTable](#csharp-xls-to-datatable)
- [C# 将XLS转换为DataTable](#csharp-convert-xls-to-datatable)
- [C# 导入XLS到DataTable](#csharp-import-xls-to-datatable)
- [C# 从XLS导出到DataTable](#csharp-export-to-datatable-from-xls)

_格式_: **XLSX**
- [C# XLSX转换为DataTable](#csharp-xlsx-to-datatable)
- [C# 将XLSX转换为DataTable](#csharp-convert-xlsx-to-datatable)
- [C# 导入XLSX到DataTable](#csharp-import-xlsx-to-datatable)
- [C# 从XLSX导出到DataTable](#csharp-export-to-datatable-from-xlsx)

_格式_: **ODS**
- [C# ODS转换为DataTable](#csharp-ods-to-datatable)
- [C# 将ODS转换为DataTable](#csharp-convert-ods-to-datatable)
- [C# 导入ODS到DataTable](#csharp-import-ods-to-datatable)
- [C# 从ODS导出到DataTable](#csharp-export-to-datatable-from-ods)

## **如何使用C#导出Excel数据**

{{% alert color="primary" %}}

本文讨论了开发人员可以通过Aspose.Cells访问的一些数据导出技术。

{{% /alert %}}

## **如何从工作表导出数据**

Aspose.Cells不仅使用户能够从外部数据源导入数据到工作表，还允许他们将工作表数据导出到一个[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)。正如我们所知，[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)是ADO.NET的一部分，并且用于保存数据。一旦数据存储在[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)中，它可以根据用户的需求以任何方式使用。如果开发人员希望，他们还可以将这些数据（存储在[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)中的数据）直接存储到数据库中。所以，我们可以看到，如果将工作表数据导出到[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)，开发人员更容易操作工作表数据。

## **如何使用Aspose.Cells将数据导出到DataTable**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类的[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)或[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)方法轻松将工作表数据导出到一个[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)对象。这两种方法在不同场景中使用，下面将更详细地讨论这些场景。

## **包含强类型数据的列**

我们知道电子表格将数据存储为一系列行和列。如果工作表的所有列中的值都是强类型的（也就是说，列中的所有值必须具有相同的数据类型），那么我们可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类的[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)方法来导出工作表内容。[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)方法以以下参数将工作表数据导出为[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)对象：

- **行号**，将要从中导出单元格数据的第一个行的行号。
- **列号**，将要从中导出数据的第一个单元格的列号。
- **行数**，要导出的行数。
- **列数**，要导出的列数。
- **导出列名**，一个布尔属性，指示是否应该将工作表的第一行数据导出为[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)的列名。

_步骤：导出数据到 DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>步骤:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>步骤:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>步骤:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>步骤:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>步骤:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>步骤:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>步骤:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>步骤:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>步骤:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>步骤:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>步骤:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>步骤:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>步骤:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>步骤:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>步骤:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>步骤:</em> Export to DataTable from ODS in C#</strong></a>

_代码步骤:_

1. 在[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)对象中加载您的Excel文件。
   - [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)对象可以加载Excel文件格式，如XLS，XLSX，XLSM，ODS等。
3. 访问Excel文件中的第一个[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/)。
4. 选择您的导出区域，例如从**DataTable**的第一个单元格开始的7行和2列。
5. 使用[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/)方法将数据导出到DataTable。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **包含非强类型数据的列**

如果工作表中的列中的所有值都不是强类型的（表示列中的值可能具有不同的数据类型），那么我们可以调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类的[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)方法导出工作表内容。[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) 方法接受与[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)方法相同的一组参数，将工作表数据导出为[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)对象。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **如何导出带标题的范围**

可以将范围的数据导出到[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)，其中有一个标志可用于跳过导出数据中的标题行。以下代码将数据范围导出到[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)，并使用一个包含[**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname)标志的参数[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions)。如果存在标题信息，它将设置为**true**，因此不会包含在数据中；如果没有标题，并且所有行都被视为数据，则设置为**false**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **高级主题**
- [以无任何格式导出Excel数据到DataTable](/cells/zh/net/export-excel-data-to-datatable-without-any-formatting/)
- [将单元格的HTML字符串值导出到DataTable](/cells/zh/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [从工作表中导出可见行数据](/cells/zh/net/export-visible-rows-data-from-worksheet/)
- [在将工作表数据导出到数据表时忽略隐藏的列](/cells/zh/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [导出工作表数据时自动重命名重复列](/cells/zh/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
{{< app/cells/assistant language="csharp" >}}

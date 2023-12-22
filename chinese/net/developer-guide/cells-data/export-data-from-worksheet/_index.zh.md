---
title: 从 .NET 中的工作表导出数据
linktitle: 从工作表导出数据
type: docs
weight: 180
url: /zh/net/export-data-from-worksheet/
description: 本文介绍如何使用 C# 将工作表中的数据导出或导入到数据表中。
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, C# Export Range with flag to skip column name
---
## 概述

本文介绍如何使用 C# 将工作表数据导出到数据表。它涵盖以下主题

_格式_：**Excel**
- [C# Excel 转数据表](#csharp-excel-to-datatable)
- [C# 将Excel转换为数据表](#csharp-convert-excel-to-datatable)
- [C# 将Excel导入数据表](#csharp-import-excel-to-datatable)
- [C# 从Excel导出到数据表](#csharp-export-to-datatable-from-excel)

_格式_：**XLS**
- [C# XLS 转至数据表](#csharp-xls-to-datatable)
- [C# 将 XLS 转换为数据表](#csharp-convert-xls-to-datatable)
- [C# 导入XLS到数据表](#csharp-import-xls-to-datatable)
- [C# 从 XLS 导出到数据表](#csharp-export-to-datatable-from-xls)

_格式_：**XLSX**
- [C# XLSX 转至数据表](#csharp-xlsx-to-datatable)
- [C# 将 XLSX 转换为数据表](#csharp-convert-xlsx-to-datatable)
- [C# 导入XLSX到数据表](#csharp-import-xlsx-to-datatable)
- [C# 从 XLSX 导出到数据表](#csharp-export-to-datatable-from-xlsx)

_格式_：**ODS**
- [C# ODS 转至数据表](#csharp-ods-to-datatable)
- [C# 将 ODS 转换为数据表](#csharp-convert-ods-to-datatable)
- [C# 导入ODS到数据表](#csharp-import-ods-to-datatable)
- [C# 从 ODS 导出到数据表](#csharp-export-to-datatable-from-ods)

##  **如何使用C#导出Excel数据**

{{% alert color="primary" %}}

本文讨论了开发者可以通过Aspose.Cells访问的一些数据导出技术。

{{% /alert %}}

##  **如何从工作表导出数据**

Aspose.Cells不仅方便用户从外部数据源将数据导入到工作表中，还允许他们将工作表数据导出到[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)。据我们所知[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)是ADO.NET的一部分，用于保存数据。一旦数据存储在[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)，可根据用户的要求采用任意方式使用。开发人员还可以存储这些数据（存储在[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)）如果他们愿意的话可以直接到数据库。因此，我们可以看到，如果将工作表数据导出到[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

##  **如何使用 Aspose.Cells 将数据导出到数据表**

开发人员可以轻松地将工作表数据导出到[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)对象通过调用[**导出数据表**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)或者[**将数据表导出为字符串**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)班级。两种方法都用于不同的场景，下面将更详细地讨论。

##  **包含强类型数据的列**

我们知道电子表格将数据存储为行和列的序列。如果工作表列中的所有值都是强类型的（这意味着列中的所有值必须具有相同的数据类型），那么我们可以通过调用导出工作表内容[**导出数据表**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)班级。[**导出数据表**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)方法采用以下参数将工作表数据导出为[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)目的：

- *行号**，将导出第一个单元格数据的行号。
- *列号**，将导出数据的第一个单元格的列号。
- *行数**，要导出的行数。
- *列数**，要导出的列数。
- *导出列名**，布尔属性，指示是否将工作表第一行的数据导出为工作表的列名[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)或不。

_步骤：导出数据到DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>脚步：</em> Excel 到 C# 中的数据表</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>脚步：</em>XLS 到 C# 中的数据表</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>脚步：</em>XLSX 到 C# 中的数据表</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>脚步：</em>ODS 到 C# 中的数据表</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>脚步：</em>将 Excel 转换为 C# 中的 DataTable</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>脚步：</em>将XLS转换为C#中的DataTable</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>脚步：</em>将XLSX转换为C#中的DataTable</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>脚步：</em>将ODS转换为C#中的DataTable</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>脚步：</em>将Excel导入到C#中的数据表</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>脚步：</em>将XLS导入到C#中的DataTable中</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>脚步：</em>将XLSX导入到C#中的DataTable中</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>脚步：</em>将ODS导入到C#中的DataTable中</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>脚步：</em>从 Excel 导出到数据表 C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>脚步：</em>从C#中的XLS导出到DataTable</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>脚步：</em>从C#中的XLSX导出到DataTable</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>脚步：</em>从C#中的ODS导出到DataTable</strong></a>

_代码步骤：_

1. 将您的 Excel 文件加载到[练习册](https://reference.aspose.com/cells/net/aspose.cells/workbook/)目的。
   - [练习册](https://reference.aspose.com/cells/net/aspose.cells/workbook/)对象可以加载Excel文件格式，例如XLS、XLSX、XLSM、ODS等。
 3. 访问第一个[工作表](https://reference.aspose.com/cells/net/aspose.cells/worksheet/)在 Excel 文件中。
4. 选择导出区域，例如从 *DataTable** 的第一个单元格开始的 7 行和 2 列。
 5. 使用[导出数据表](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/)方法将数据导出到DataTable。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

##  **包含非强类型数据的列**

如果工作表列中的所有值都不是强类型的（这意味着列中的值可能具有不同的数据类型），那么我们可以通过调用导出工作表内容[**将数据表导出为字符串**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)班级。[**将数据表导出为字符串**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)方法采用与方法相同的参数集[**导出数据表**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)将工作表数据导出为[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)目的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

##  **如何使用标志导出范围以跳过列名称**

某个范围内的数据可以导出到[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)其中有一个标志可用于跳过导出数据中的标题行。以下代码将一系列数据导出到[**数据表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)有争论[**导出表选项**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions)其中包含[**导出列名称**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname)旗帜。它被设置为**真的**如果存在标头信息，则它不会包含在数据中并设置为**错误的**如果没有标题并且所有行都被视为数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

##  **高级主题**
- [将 Excel 数据导出到 DataTable，无需任何格式](/cells/zh/net/export-excel-data-to-datatable-without-any-formatting/)
- [将 Cells 的 HTML 字符串值导出到数据表](/cells/zh/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [从工作表导出可见行数据](/cells/zh/net/export-visible-rows-data-from-worksheet/)
- [将工作表数据导出到数据表时忽略隐藏列](/cells/zh/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [导出工作表数据时自动重命名重复列](/cells/zh/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)

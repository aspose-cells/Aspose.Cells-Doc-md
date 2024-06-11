---
title: 将数据导入工作表
type: docs
weight: 170
url: /zh/net/import-data-into-worksheet/
description: 了解如何通过 Aspose.Cells for .NET API 将数据导入工作表。
keywords: C# 将数据导入工作表，使用 ICellsDataTable 接口将数据导入 Excel，从数组导入数据，从 ArrayList 导入数据，从自定义对象导入数据，将数据从自定义对象导入合并区域，从 DataTable 导入数据，从动态对象作为数据源导入数据，从 DataColumn 导入数据，从 DataView 导入数据，从 DataGrid 导入数据，从 GridView 导入数据，从 HTML 格式化数据导入，从 JSON 导入数据
---

{{% alert color="primary" %}}

本文讨论了开发人员通过 Aspose.Cells 可以访问的一些数据导入技术。

{{% /alert %}}

## **如何将数据导入工作表**

当您使用 Aspose.Cells 打开 Excel 文件时，文件中的所有数据都会被自动导入。Aspose.Cells 还可以从其他数据源导入数据。

Aspose.Cells 提供了一个代表 Microsoft Excel 文件的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问 Excel 文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了从不同数据源导入数据的有用方法。本文解释了如何使用这些方法。

## **如何使用ICellsDataTable接口将数据导入Excel**
实现[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)以包装不同的数据源，然后使用[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata)将数据导入到Excel工作表中。
### **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

给出*CustomerDataSource*、*Customer*和*CustomerList*类的实现如下

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **如何从数组导入数据到Excel**

要从数组导入数据到电子表格，调用[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)集合的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)方法。[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)方法有很多重载版本，但典型的重载方法需要以下参数:

- **数组**，您正在从中导入内容的数组对象。
- **行号**，将导入数据到其中的第一个单元格的行号。
- **列号**，将导入数据到其中的第一个单元格的列号。
- **Is vertical**，指定是垂直还是水平导入数据的布尔值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **如何从ArrayList导入数据到Excel**

要将数据从*ArrayList*导入到工作表中，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)方法。ImportArray方法接受以下参数:

- **数组列表**，表示要导入的*ArrayList*对象。
- **行号**，表示将要导入数据的第一个单元格的行号。
- **列号**，表示要导入数据的第一个单元格的列号。
- **Is vertical**，指定是垂直还是水平导入数据的布尔值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **如何从自定义对象导入数据到Excel**

要从对象集合导入数据到工作表，请使用[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index)。提供一列/属性列表给该方法，以显示您想要的对象列表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **如何从自定义对象导入数据到Excel并检查合并区域**

要将数据从对象集合导入到包含合并单元格的工作表中，请使用*[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)*属性。如果Excel模板有合并单元格，请将[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)属性的值设置为true。将[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)对象连同列/属性列表传递给方法以显示您想要的对象列表。以下代码示例演示了如何使用*[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)*属性将数据从自定义对象导入到合并单元格。请参阅附加的[source Excel](90112033.xlsx)文件和[output Excel](90112034.xlsx)文件供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **如何从DataTable导入数据到Excel**

要从*DataTable*导入数据，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)方法。[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)方法有很多重载版本，但典型的重载方法需要以下参数:

- **数据表**，您从中导入内容的*DataTable*对象。
- **是否显示字段名**，指定是否将*DataTable*的列名称作为第一行导入工作表。
- **起始单元格**，表示从那里导入*DataTable*内容的起始单元格的名称(例如"A1")。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **如何从动态对象作为数据源导入数据到Excel**

Aspose.Cells提供了与动态对象一起使用的功能作为数据源。它有助于使用动态地向对象添加属性的数据源。一旦属性被添加到对象中，Aspose.Cells会将第一个条目视为模板并相应处理其余条目。这意味着如果某些动态属性仅添加到第一个项目而不添加到其他对象，则Aspose.Cells会认为集合中的所有项应该相同。

在这个例子中，首先使用了模板模型，其中只包含两个变量。这个List被转换为动态对象List。然后一些额外字段被添加到其中，最后加载到工作簿。工作簿仅选择模板XLSX文件中的那些值。这个模板工作簿使用智能标记器，它也包含参数。 参数允许您修改信息的布局方式。有关智能标记器的详细信息，请参考以下文章:

[使用智能标记](/cells/zh/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **如何将DataColumn导入到Excel**

*DataTable*或*DataView*对象由一个或多个列组成。开发人员还可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法从*DataTable*或*DataView*中的任何列/列导入数据。[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法接受类型为[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)的参数。[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)类提供了一个[**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)属性，接受一个列索引数组。

下面给出的示例代码演示了使用[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)来导入选择性列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **如何将DataView导入到Excel**

要从*DataView*导入数据，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法。[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法有很多重载版本，但DataView的一个版本接受以下参数：

- **DataView:** 将要从中导入内容的*DataView*对象。
- **第一行:** 数据将导入到的第一个单元格的行号。
- **第一列:** 数据将导入到的第一个单元格的列号。
- **ImportTableOptions:** 导入选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **如何将DataGrid导入到Excel**

可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)方法从*DataGrid*导入数据。[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)方法有许多重载版本，但典型的重载接受以下参数：

- **数据表格**，要从中导入内容的*DataGrid*对象。
- **行号**，数据将导入到的第一个单元格的行号。
- **列号**，数据将导入到的第一个单元格的列号。
- **插入行**，一个布尔属性，指示是否应向工作表添加额外行以适应数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **如何将GridView导入到Excel**

要从*GridView*控件导入数据，调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview)方法。

Aspose.Cells允许我们在导入数据到电子表格时尊重HTML格式化的值。在导入数据时启用HTML解析时，Aspose.Cells将HTML转换为相应的单元格格式。

## **如何将HTML格式化数据导入Excel**

Aspose.Cells提供一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类，提供了非常有用的方法，用于从外部数据源导入数据。本文显示了如何在导入数据时解析HTML格式的文本并将HTML转换为格式化的单元格值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **如何从JSON导入数据到Excel**

Aspose.Cells为处理JSON提供了一个[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)类。[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)类具有一个导入JSON数据的[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)方法。Aspose.Cells还提供了一个表示JSON布局选项的[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)类。[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)方法接受[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)作为参数。[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)类提供以下属性。

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)：指示数组是否应处理为表格。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate)：获取或设置一个值，指示JSON中的字符串是否要转换为数字或日期。
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat)：获取和设置日期值的格式。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)：指示是否应忽略对象的属性标题是否为数组。
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull)：指示是否应忽略空值。
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle)：指示是否应忽略对象的属性标题是否为对象。
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat)：获取和设置数值的格式。
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle)：获取和设置标题的样式。

下面给出的示例代码演示了使用[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)和[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)类来导入JSON数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **高级主题**
- [在将数据导入工作表时指定公式字段](/cells/zh/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [在插入单元格数据表行时将第一行下移](/cells/zh/net/shift-first-row-down-when-inserting-cells-data-table-rows/)

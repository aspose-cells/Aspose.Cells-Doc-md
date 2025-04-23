---
title: 工作表中导入数据
type: docs
weight: 170
url: /zh/net/import-data-into-worksheet/
description: 学习如何通过 Aspose.Cells for .NET API 将数据导入工作表。
keywords: C# 将数据导入工作表，通过 ICellsDataTable 接口将数据导入 Excel，从数组导入数据，从 ArrayList 导入数据，从自定义对象导入数据，将自定义对象数据导入到合并区域，从 DataTable 导入数据，将动态对象作为数据源导入数据，从 DataColumn 导入数据，从 DataView 导入数据，从 DataGrid 导入数据，从 GridView 导入数据，导入 HTML 格式数据，从 JSON 导入数据
---

{{% alert color="primary" %}}

本文讨论了一些开发人员可以通过 Aspose.Cells 访问的数据导入技术。

{{% /alert %}}

## **如何将数据导入工作表**

使用 Aspose.Cells 打开 Excel 文件时，文件中的所有数据都会自动导入。Aspose.Cells 还可以从其他数据源导入数据。

Aspose.Cells 提供了一个 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 表示 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，该集合允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提SUPPLIEDBY[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合提供了从不同数据源导入数据的有用方法。本文介绍了如何使用这些方法。

## **通过实现 [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) 来包装各种数据源，然后使用 [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) 将数据导入到 Excel 工作表。**
通过实现 [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) 来包装各种数据源，然后使用 [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) 将数据导入到 Excel 工作表。
### **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

给出了*CustomerDataSource*、*Customer*和*CustomerList*类的实现

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **如何将数组数据导入Excel**

要从数组导入数据到电子表格，调用 [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) 集合的 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 方法。 [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) 方法有许多重载版本，但典型的重载采用以下参数:

- **Array**，要从中导入内容的数组对象。
- **行号**，第一个单元格的行号，数据将被导入到该单元格。
- **列号**，第一个单元格的列号，数据将被导入到该单元格。
- **是否垂直**，指定是垂直还是水平导入数据的布尔值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **如何将 ArrayList 中的数据导入 Excel**

要从 *ArrayList* 导入数据到工作表，请调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合的 [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist) 方法。ImportArray 方法需要以下参数：

- **ArrayList**，代表要导入的 *ArrayList* 对象。
- **行号**，代表将要导入数据的第一个单元格的行号。
- **列号**，代表将要导入数据的第一个单元格的列号。
- **是否垂直**，指定是垂直还是水平导入数据的布尔值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **如何从自定义对象导入数据到Excel**

要从对象集合导入数据到工作表，请使用 [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index)。向该方法提供一个列名/属性列表，以显示您所需的对象列表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **如何从自定义对象以及检查合并区域导入数据到Excel**

要从对象集合导入数据到包含合并单元格的工作表中，请使用 [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) 属性。如果Excel模板中有合并单元格，请将 [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) 属性的值设置为 true。将 [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) 对象与列名/属性列表一起传递给方法，以显示您所需的对象列表。以下代码示例演示了使用 [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) 属性将自定义对象的数据导入到合并单元格中。请参阅附加的 [源Excel](90112033.xlsx) 文件和 [输出Excel](90112034.xlsx) 文件以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **如何从DataTable导入数据到Excel**

要从 *DataTable* 导入数据，请调用 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 集合的 [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) 方法。 [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) 方法有很多重载版本，但典型的重载接受以下参数：

- **DataTable**，要从中导入内容的 *DataTable* 对象。
- **是否显示字段名**，指定 *DataTable* 的列名是否应导入到工作表作为首行。
- **起始单元格**，表示应从其中导入 *DataTable* 内容的起始单元格的名称（例如“A1”）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **如何从动态对象作为数据源导入数据到Excel**

Aspose.Cells提供了处理动态对象作为数据源的功能。它有助于在对象动态添加属性的情况下使用数据源。一旦属性被添加到对象中，Aspose.Cells将第一个条目视为模板并相应处理其他条目。这意味着如果某些动态属性仅添加到第一个项目而未添加到其他对象，则Aspose.Cells将认为集合中的所有项目应该是相同的。

在这个例子中，使用了最初仅包含两个变量的模板模型。这个列表被转换成动态对象列表。然后一些额外的字段被添加进去，最后加载到工作簿中。工作簿仅选择模板XLSX文件中的值。这个模板工作簿使用了智能标记器，它还包含参数。参数允许您修改信息布局的方式。关于智能标记器的详细信息可以从以下文章中获取：

[使用智能标记器](/cells/zh/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **如何将DataColumn导入Excel**

一个 *DataTable* 或 *DataView* 对象由一个或多个列组成。开发人员还可以通过调用 [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) 集合的 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) 方法从 *DataTable* 或 *DataView* 中导入任何列/列的数据。 [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) 方法接受 [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) 类型的参数。 [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) 类提供了 [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) 属性，该属性接受一个列索引的数组。

下面提供的示例代码演示了使用 [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) 来导入选择性列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **如何将DataView导入Excel**

要从DataView导入数据，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法。 [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法有多个重载版本，但DataView的版本需要以下参数：

- DataView: 您将要从中导入内容的 DataView 对象。
- First Row: 数据将要导入到的第一个单元格的行号。
- First Column: 数据将要导入到的第一个单元格的列号。
- ImportTableOptions: 导入选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **如何将DataGrid导入Excel**

可以通过调用集合的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)方法从DataGrid导入数据。 [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)方法有多个重载版本，但典型的重载版本需要以下参数：

- Data grid, 要从中导入内容的 DataGrid 对象。
- Row Number, 数据将要导入到的第一个单元格的行号。
- Column Number, 数据将要导入到的第一个单元格的列号。
- Insert Rows, 一个布尔属性，指示是否应向工作表添加额外行以适应数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **如何将GridView导入Excel**

要从GridView控件导入数据，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview)方法。

Aspose.Cells允许我们在导入数据到电子表格时尊重HTML格式化的值。当导入数据时启用HTML解析时，Aspose.Cells将HTML转换为相应的单元格格式。

## **如何将HTML格式化数据导入Excel**

Aspose.Cells提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类，为从外部数据源导入数据提供了非常有用的方法。本文展示了在导入数据时如何解析HTML格式化文本并将HTML转换为格式化的单元格值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **如何将数据从JSON导入Excel**

Aspose.Cells为处理JSON提供了一个[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)类。[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)类具有一个用于导入JSON数据的[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)方法。 Aspose.Cells还提供了一个代表JSON布局选项的[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)类。 [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)方法接受[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)为参数。 [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)类提供以下属性。

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)：指示是否应将数组处理为表格。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): 获取或设置一个值，指示JSON中的字符串是否要转换为数字或日期。
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat)：获取和设置日期值的格式。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): 指示是否忽略对象属性为数组时的标题。
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull)：指示是否应忽略空值。
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): 指示是否忽略对象属性为对象时的标题。
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat)：获取和设置数值值的格式。
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle)：获取和设置标题的样式。

下面给出的示例代码演示了使用 [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) 和 [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) 类来导入JSON数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **高级主题**
- [在工作表导入数据时指定公式字段](/cells/zh/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [将单元格数据表行插入时将第一行向下移动](/cells/zh/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
{{< app/cells/assistant language="csharp" >}}

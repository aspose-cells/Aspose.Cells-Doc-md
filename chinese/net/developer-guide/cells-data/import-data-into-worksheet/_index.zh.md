---
title: 将数据导入工作表
type: docs
weight: 170
url: /zh/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

本文讨论开发者通过Aspose.Cells接触到的一些数据导入技巧。

{{% /alert %}}

## **将数据导入工作表**

当您打开带有 Aspose.Cells 的 Excel 文件时，文件中的所有数据都会自动导入。 Aspose.Cells也可以从其他数据源导入数据。

Aspose.Cells提供了[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection 提供了从不同数据源导入数据的有用方法。本文解释了如何使用这些方法。

## **使用 ICellsDataTable 接口将数据导入 Excel**
实施[ICells数据表](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)包装您的各种数据源，然后使用[Cells.导入数据（）](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata)将数据导入 Excel 工作表。
### **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

实施*客户数据源*, *顾客*， 和*客户名单*课程如下

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **从数组导入**

要将数据从数组导入电子表格，请调用[**导入数组**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。有许多重载版本[**导入数组**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)方法，但典型的重载采用以下参数：

- **大批**，您要从中导入内容的数组对象。
- **行号**，数据将导入到的第一个单元格的行号。
- **列号**，数据将导入到的第一个单元格的列号。
- **是垂直的**一个布尔值，指定是垂直导入数据还是水平导入数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **从 ArrayList 导入**

从中导入数据*数组列表*到工作表，调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**导入数组列表**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)方法。 ImportArray 方法采用以下参数：

- **数组列表** , 代表*数组列表*您正在导入的对象。
- **行号**, 表示数据将导入到的第一个单元格的行号。
- **列号**, 表示数据将导入到的第一个单元格的列号。
- **是垂直的**一个布尔值，指定是垂直导入数据还是水平导入数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **从自定义对象导入**

要将对象集合中的数据导入工作表，请使用[**导入自定义对象**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index).向方法提供列/属性列表以显示所需的对象列表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **从自定义对象导入到合并区域**

要将对象集合中的数据导入包含合并单元格的工作表，请使用[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)财产。如果Excel模板有合并单元格，设置值[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)属性为真。通过[**导入表选项**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)对象连同列/属性列表一起添加到显示所需对象列表的方法中。下面的代码示例演示了使用[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)属性将数据从自定义对象导入到合并的单元格。请参阅附件[源Excel](90112033.xlsx)文件和[输出Excel](90112034.xlsx)文件供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **从数据表导入**

从中导入数据*数据表* 调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**导入数据表**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)方法。有许多重载版本[**导入数据表**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)方法，但典型的重载采用以下参数：

- **数据表** ， 这*数据表*您从中导入内容的对象。
- **是否显示字段名称** 指定是否名称*数据表*列是否应该作为第一行导入到工作表中。
- **起始细胞** 表示从中导入内容的起始单元格的名称（例如“A1”）*数据表*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **从动态对象导入作为数据源**

Aspose.Cells 提供将动态对象用作数据源的功能。它有助于使用将属性动态添加到对象的数据源。将属性添加到对象后，Aspose.Cells 会将第一个条目视为模板并相应地处理其余条目。这意味着如果某些动态属性仅添加到第一个项目而不是其他对象，Aspose.Cells 认为集合中的所有项目都应该相同。

在这个例子中，使用了一个模板模型，它最初只包含两个变量。此列表转换为动态对象列表。然后将一些额外的字段添加到其中并最终加载到工作簿中。工作簿仅选取模板 XLSX 文件中的那些值。此模板工作簿使用也包含参数的智能标记。参数允许您修改信息的布局方式。有关智能标记的详细信息，请参阅以下文章：

[使用智能标记](/cells/zh/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **从 DataColumn 导入 (.NET)**

一个*数据表*或者*数据视图*对象由一列或多列组成。开发人员还可以从任何 Column/Columns 中导入数据*数据表*或者*数据视图*通过调用[**导入数据**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**导入数据**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法接受类型参数[**导入表选项**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions).这[**导入表选项**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)类提供了[**列索引**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)接受列索引数组的属性。

下面给出的示例代码演示了使用[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)导入选择性列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **从 DataView 导入 (.NET)**

从中导入数据*数据视图* 调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏的[**导入数据**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法。有许多重载版本[**导入数据**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法，但 DataView 的方法采用以下参数：

- **数据视图：**这*数据视图*您要从中导入内容的对象。
- **第一排：**数据将导入到的第一个单元格的行号。
- **第一栏：**数据将导入到的第一个单元格的列号。
- **导入表选项：**导入选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **从 DataGrid 导入 (.NET)**

可以从一个导入数据*数据网格*通过调用[**导入数据网格**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。有许多重载版本[**导入数据网格**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)方法，但典型的重载采用以下参数：

- **数据网格** ， 这*数据网格*您从中导入内容的对象。
- **行号**，数据将导入到的第一个单元格的行号。
- **列号**，数据将导入到的第一个单元格的列号。
- **插入行**一个布尔属性，指示是否应将额外的行添加到工作表以适合数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **从 GridView 导入**

从中导入数据*网格视图*控制，调用[**导入网格视图**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。

Aspose.Cells 允许我们在将数据导入电子表格时遵循 HTML 格式的值。在导入数据时启用 HTML 解析时，Aspose.Cells 会将 HTML 转换为相应的单元格格式。

## **导入 HTML 格式的数据**

Aspose.Cells提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)提供从外部数据源导入数据的非常有用的方法的类。本文介绍如何在导入数据时解析 HTML 格式的文本，并将 HTML 转换为格式化的单元格值。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **从 JSON 导入数据**

Aspose.Cells提供了[**Json工具**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)处理JSON的类。[**Json工具**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)类有一个[**导入数据**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)导入JSON数据的方法。 Aspose.Cells还提供了[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)表示 JSON 布局选项的类。这[**导入数据**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)方法接受[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)作为参数。这[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)类提供以下属性。

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)：表示数组中是否作为表格处理。
- [**转换数字或日期**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate)：获取或设置一个值，该值表示将JSON中的字符串转换为数值型还是日期型。
- [**日期格式**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat)：获取和设置日期值的格式。
- [**忽略数组标题**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): 表示如果对象的属性是数组，是否忽略标题
- [**忽略空值**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull)：指示是否应忽略空值。
- [**忽略对象标题**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle)表示如果对象的属性是对象，是否忽略标题。
- [**数字格式**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat)：获取和设置数值的格式。
- [**标题样式**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle)获取和设置标题的样式。

下面给出的示例代码演示了使用[**Json工具**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)和[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)用于导入 JSON 数据的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **推进主题**
- [将数据导入工作表时指定公式字段](/cells/zh/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [插入 Cells 数据表行时将第一行向下移动](/cells/zh/net/shift-first-row-down-when-inserting-cells-data-table-rows/)

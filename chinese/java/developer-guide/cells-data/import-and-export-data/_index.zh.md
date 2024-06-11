---
title: 导入和导出数据
type: docs
weight: 130
url: /zh/java/import-and-export-data/
---

{{% alert color="primary" %}}

本文讨论了一些开发人员可以通过 Aspose.Cells 访问的数据导入和导出技术。

{{% /alert %}}

## 将数据导入工作表

数据代表现实世界。为了理解数据，我们对其进行分析，并了解世界。数据转化为信息。

进行分析的方法有许多种：将数据放入电子表格并以不同方式操纵它是一种常见的方法。有了 Aspose.Cells，我们可以轻松创建电子表格，从各种外部来源获取数据并为分析做准备。

本文讨论了一些开发人员可以通过 Aspose.Cells 访问的数据导入技术。

### 使用 Aspose.Cells 导入数据

当您使用 Aspose.Cells 打开 Excel 文件时，文件中的所有数据会自动导入。Aspose.Cells 还可以从其他数据源导入数据:

- [数组](/cells/zh/java/import-and-export-data/).
- [数组列表](/cells/zh/java/import-and-export-data/).
- [结果集](/cells/zh/java/import-and-export-data/).
- [JSON](/cells/zh/java/import-and-export-data/)

Aspose.Cells提供了一个代表Microsoft Excel文件的类——[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合，该集合允许访问Excel文件中的每个工作表，工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示，[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合，[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合提供了从其他数据源导入数据的非常有用的方法。本文介绍了如何使用这些方法。

#### 从数组导入

要从数组导入数据到电子表格，调用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合的importArray方法。importArray方法有很多重载版本，但典型的重载需要以下参数：

- **Array**，要从中导入内容的数组对象。
- **行号**，第一个单元格的行号，数据将被导入到该单元格。
- **列号**，第一个单元格的列号，数据将被导入到该单元格。
- **是否垂直**，指定是垂直还是水平导入数据的布尔值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### 从多维数组导入

要从多维数组导入数据到电子表格，调用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合的相关importArray重载：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### 从ArrayList导入

要将*ArrayList*中的数据导入到工作表，调用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合的[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)方法。[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)方法需要以下参数：

- **ArrayList**，要导入内容的*ArrayList*对象。
- **行号**，将导入内容的单元格范围的第一个单元格的行号。
- **列号**，将导入数据的第一个单元格的列号。
- **是否垂直**，指定是垂直还是水平导入数据的布尔值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### 将自定义对象导入到合并区域

要从包含合并单元格的工作表中导入对象集的数据，请使用[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性。如果Excel模板具有合并单元格，请将[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性的值设置为true。将[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)对象与要显示的对象列表/属性一起传递给方法。以下代码示例演示了使用[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性从自定义对象导入数据到合并单元格。请参阅附加的[source Excel](90112035.xlsx)文件和[output Excel](90112036.xlsx)文件进行参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### 从JSON导入数据

Aspose.Cells提供了一个[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类来处理JSON。[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类具有一个[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)方法用于导入JSON数据。Aspose.Cells还提供了一个[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类，表示JSON布局的选项。[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)方法接受[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)作为参数。[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类提供以下属性。

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)：指示是否应将数组处理为表格。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate)：获取或设置一个值，指示JSON中的字符串是否应转换为数值或日期。
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat)：获取和设置日期值的格式。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)：指示是否要忽略对象的属性是数组时的标题。
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull)：指示是否应忽略空值。
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle)：指示是否要忽略对象的属性是对象时的标题。
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat)：获取和设置数值值的格式。
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle)：获取和设置标题的样式。

下面给出的示例代码演示了使用[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)和[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类来导入JSON数据的用法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## 从工作表导出数据

Aspose.Cells不仅允许用户从外部数据源将数据导入到工作表中，还允许他们将工作表数据导出为数组。

### 使用Aspose.Cells导出数据 - 将数据导出到数组

Aspose.Cells提供了一个表示Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合。

数据可以使用 [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) 类的 [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) 方法轻松导出到一个数组对象中。

#### 包含强类型数据的列

电子表格将数据存储为行和列的序列。使用 [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) 方法将工作表中的数据导出为一个数组。[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) 使用以下参数将工作表数据导出为 *Array* 对象:

- 行数，数据将从第一个单元格导出的行号。
- 列数，数据将从第一个单元格导出的列号。
- 行数，要导出的行数。
- 列数，要导出的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **高级主题**
- [从 Microsoft Access 数据库 ResultSet 对象导入数据到工作表](/cells/zh/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [在工作表导入数据时指定公式字段](/cells/zh/java/specify-formula-fields-while-importing-data-to-worksheet/)

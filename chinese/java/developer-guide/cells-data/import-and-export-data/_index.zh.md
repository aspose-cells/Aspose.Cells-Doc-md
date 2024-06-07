---
title: 导入和导出数据
type: docs
weight: 130
url: /zh/java/import-and-export-data/
---

{{% alert color="primary" %}}

本文讨论开发人员通过Aspose.Cells可以访问的一些数据导入和导出技术。

{{% /alert %}}

##将数据导入工作表

数据代表着世界的样子。要理解数据，我们需要分析数据并对世界有所了解。数据变成信息。

有许多分析的方法：将数据放入电子表格并以不同方式操纵它是常用的方法之一。使用Aspose.Cells，可以轻松创建从各种外部来源获取数据并准备进行分析的电子表格。

本文讨论了开发人员通过 Aspose.Cells 可以访问的一些数据导入技术。

###使用Aspose.Cells导入数据

当使用Aspose.Cells打开Excel文件时，文件中的所有数据都将自动导入。Aspose.Cells还可以从其他数据源导入数据：

- [Array](/cells/zh/java/import-and-export-data/).
- [Array list](/cells/zh/java/import-and-export-data/).
- [Result set](/cells/zh/java/import-and-export-data/).
- [JSON](/cells/zh/java/import-and-export-data/)

Aspose.Cells提供了一个[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，该类表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合提供了从其他数据源导入数据的非常有用的方法。本文将解释如何使用这些方法。

#### 从数组导入

要从数组导入数据到电子表格，请调用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合的importArray方法。 importArray方法有多个重载版本，但典型的重载版本接受以下参数：

- **数组**，您正在从中导入内容的数组对象。
- **行号**，将导入数据到其中的第一个单元格的行号。
- **列号**，将导入数据到其中的第一个单元格的列号。
- **Is vertical**，指定是垂直还是水平导入数据的布尔值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### 从多维数组导入

要从多维数组导入数据到电子表格，请调用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合的相关importArray重载：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### 从ArrayList导入

要将数据从*ArrayList*导入到工作表，请调用[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)）方法，并将[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合传递给[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean))方法。 [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean))方法需要以下参数：

- **ArrayList**，要导入其内容的*ArrayList*对象。
- **行号**，要从中导入内容的单元格范围的第一个单元格的行号。
- **列号**，从中导入数据的第一个单元格的列号。
- **Is Vertical**，一个布尔值，指定是纵向还是横向导入数据。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### 从自定义对象导入到合并区域

要将对象集合的数据导入到包含合并单元格的工作表中，请使用[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性。如果Excel模板有合并单元格，请将[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性的值设置为true。传递[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)对象以及要显示所需对象列表的列/属性列表到方法。以下代码示例演示了将数据从自定义对象导入到合并单元格的[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性的使用。请参阅附加的[source Excel](90112035.xlsx)文件和输出的[Excel文件](90112036.xlsx)以供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### 从JSON导入数据

Aspose.Cells为处理JSON提供了一个[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类。[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类有一个[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions))方法来导入JSON数据。Aspose.Cells还提供了一个[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类来表示JSON布局的选项。[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions))方法接受[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)作为参数。[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类提供以下属性。

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)：指示数组是否应处理为表格。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate)：获取或设置指示是否将JSON中的字符串转换为数字或日期的值。
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat)：获取和设置日期值的格式。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)：指示是否忽略对象的属性为数组的标题
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull)：指示是否应忽略空值。
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle)：指示是否忽略对象的属性为对象的标题。
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat)：获取和设置数值的格式。
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle)：获取和设置标题的样式。

下面给出的示例代码演示了使用[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)和[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类导入JSON数据。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## 从工作表导出数据

Aspose.Cells不仅让用户可以从外部数据源导入数据表中，还允许他们将工作表数据导出到数组中。

### 使用Aspose.Cells导出数据 - 将数据导出到数组

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合。

可以使用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)类的[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int))方法轻松将数据导出到数组对象。

#### 包含强类型数据的列

电子表格将数据存储为行和列的序列。使用[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int))方法将工作表中的数据导出为*Array*对象。[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int))接受以下参数来导出工作表数据为*Array*对象：

- 行号，数据将从第一个单元格导出的行号。
- 列号，数据将从哪个列开始导出的列号。
- 行数，要导出的行数。
- 列数，要导出的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **高级主题**
- [将数据从Microsoft Access数据库结果集对象导入到工作表](/cells/zh/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [在将数据导入工作表时指定公式字段](/cells/zh/java/specify-formula-fields-while-importing-data-to-worksheet/)

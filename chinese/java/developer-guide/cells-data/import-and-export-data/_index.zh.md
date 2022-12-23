---
title: 进出口数据
type: docs
weight: 130
url: /zh/java/import-and-export-data/
---
{{% alert color="primary" %}}

本文讨论开发者通过Aspose.Cells接触到的一些数据导入导出技术。

{{% /alert %}}

## 将数据导入工作表

数据代表了世界的本来面目。为了理解数据，我们对其进行分析并了解世界。数据变成信息。

执行分析的方法有很多种：将数据放入电子表格并以不同方式对其进行处理是一种常见的方法。使用 Aspose.Cells，可以轻松创建电子表格，从一系列外部来源获取数据并准备用于分析。

本文讨论开发者通过Aspose.Cells接触到的一些数据导入技巧。

### 使用 Aspose.Cells 导入数据

当您打开带有 Aspose.Cells 的 Excel 文件时，文件中的所有数据都会自动导入。 Aspose.Cells也可以从其他数据源导入数据：

- [大批](/cells/zh/java/import-and-export-data/).
- [数组列表](/cells/zh/java/import-and-export-data/).
- [结果集](/cells/zh/java/import-and-export-data/).
- [JSON](/cells/zh/java/import-and-export-data/)

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含集合[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)这允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)收藏。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合为从其他数据源导入数据提供了非常有用的方法。本文解释了如何使用这些方法。

#### 从数组导入

要将数据从数组导入电子表格，请调用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)收藏。 importArray 方法有许多重载版本，但典型的重载采用以下参数：

- **大批**，您要从中导入内容的数组对象。
- **行号**，数据将导入到的第一个单元格的行号。
- **列号**，数据将导入到的第一个单元格的列号。
- **是垂直的**一个布尔值，指定是垂直导入数据还是水平导入数据。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### 从多维数组导入

要将数据从多维数组导入电子表格，请调用相关的 importArray 重载[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)收藏：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### 从 ArrayList 导入

从中导入数据*数组列表*到工作表，调用[**导入数组列表**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) 的方法[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)收藏。这[**导入数组列表**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)方法采用以下参数：

- **数组列表** ， 这*数组列表*其内容将被导入的对象。
- **行号**将从中导入内容的单元格范围的第一个单元格的行号。
- **列号**将从中导入数据的第一个单元格的列号。
- **是垂直的**是一个布尔值，指定是垂直导入数据还是水平导入数据。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### 从自定义对象导入到合并区域

要将对象集合中的数据导入包含合并单元格的工作表，请使用[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)财产。如果Excel模板有合并单元格，设置值[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性为真。通过[**导入表选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)对象连同列/属性列表一起添加到显示所需对象列表的方法中。下面的代码示例演示了使用[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)属性将数据从自定义对象导入到合并的单元格。请参阅附件[源Excel](90112035.xlsx)文件和[输出Excel](90112036.xlsx)文件供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### 从 JSON 导入数据

Aspose.Cells提供了[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)处理类 JSON。[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类有一个[**导入数据**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) 导入JSON数据的方法。 Aspose.Cells还提供了[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)表示 JSON 布局选项的类。这[**导入数据**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) 方法接受[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)作为参数。这[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类提供以下属性。

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)：表示数组中是否作为表格处理。
- [**转换数字或日期**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate)获取或设置一个值，该值指示JSON中的字符串是转换为数字还是日期。
- [**日期格式**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat)：获取和设置日期值的格式。
- [**忽略数组标题**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)表示如果对象的属性是数组，是否忽略标题
- [**忽略空值**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull)：指示是否应忽略空值。
- [**忽略对象标题**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle)表示如果对象的属性是对象，是否忽略标题。
- [**数字格式**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat)：获取和设置数值的格式。
- [**标题样式**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle)获取和设置标题的样式。

下面给出的示例代码演示了使用[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)和[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)导入 JSON 数据的类。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## 从工作表导出数据

Aspose.Cells 不仅允许其用户将数据从外部数据源导入工作表，还允许他们将工作表数据导出到数组。

### 使用 Aspose.Cells 导出数据 - 将数据导出到数组

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)收藏。

使用以下方法可以轻松地将数据导出到数组对象[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)班级'[**导出数组**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)） 方法。

#### 包含强类型数据的列

电子表格将数据存储为一系列行和列。使用[**导出数组**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) 方法将数据从工作表导出到数组。[**导出数组**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) 采用以下参数将工作表数据导出为*大批*目的：

- 行号，数据将从中导出的第一个单元格的行号。
- 列号，数据将从中导出的第一个单元格的列号
- Number of rows，要导出的行数。
- Number of columns，要导出的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **推进主题**
- [将数据从 Microsoft Access 数据库结果集对象导入到工作表](/cells/zh/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [将数据导入工作表时指定公式字段](/cells/zh/java/specify-formula-fields-while-importing-data-to-worksheet/)

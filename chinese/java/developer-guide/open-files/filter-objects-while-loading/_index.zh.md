---
title: 在加载工作簿或工作表时过滤对象
type: docs
weight: 1060
url: /zh/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **可能的使用场景**
在从工作簿中过滤数据时，请使用 [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) 属性。但是，如果要从单独的工作表中过滤数据，则必须重写 [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\)) 方法。在创建或处理 [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter) 时，请使用 [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) 枚举中的适当值。

[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) 枚举具有以下值。

- [无](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [全部](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [空单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [字符串单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [数值单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [错误单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [布尔单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [值单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [公式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [数据单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [图表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [形状](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [合并区域](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [条件格式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [数据验证](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [数据透视表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [表格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [超链接](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [工作表设置](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [工作表数据](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [工作簿设置](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [设置](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML 映射](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [结构](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [文档属性](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [定义名称](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [样式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **在加载工作簿时筛选对象**
以下示例代码演示了如何从工作簿中筛选图表。请查看此代码中使用的示例 Excel 文件和生成的输出 PDF。如您在输出 PDF 中所见，所有图表都已从工作簿中筛选出。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **在加载工作表时过滤对象**
以下示例代码加载[源Excel文件](5472492.xlsx)并使用自定义筛选器从其工作表中过滤以下数据。

- 它会从名为NoCharts的工作表中筛选图表。
- 它会从名为NoShapes的工作表中筛选形状。
- 它会从名为NoConditionalFormatting的工作表中筛选条件格式。

一旦带有自定义筛选器加载[源Excel文件](5472492.xlsx)，它逐个获取所有工作表的图像。以下是供您参考的输出图像。正如您所见，第一个图像没有图表，第二个图像没有形状，第三个图像没有条件格式。

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}

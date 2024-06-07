---
title: 加载工作簿或工作表时筛选对象
type: docs
weight: 1060
url: /zh/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **可能的使用场景**
在从工作簿中筛选数据时，请使用[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) 属性。如果要从单个工作表中筛选数据，则必须重写[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\)) 方法。在创建或处理[LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter) 时，请使用[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) 枚举中的适当值。

[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) 枚举具有以下值。

- [无](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [全部](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [公式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [图表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [形状](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [合并区域](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [条件格式设置](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [数据验证](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [数据透视表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
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
## **在加载工作簿时过滤对象**
以下示例代码说明了如何过滤工作簿中的图表。请查看此代码中使用的 [样本excel文件](5472489.xlsx) 以及由此生成的 [输出PDF](5472488.pdf)。正如您在输出PDF中所看到的，所有图表都已从工作簿中过滤出来。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **在加载工作表时过滤对象**
以下示例代码加载 [源excel文件](5472492.xlsx) 并使用自定义过滤器从其工作表中过滤以下数据。

- 从名为NoCharts的工作表中筛选图表。
- 从名为NoShapes的工作表中筛选形状。
- 从名为NoConditionalFormatting的工作表中筛选条件格式。

一旦使用自定义过滤器加载 [源excel文件](5472492.xlsx) ，它将逐一获取所有工作表的图像。以下是供您参考的输出图像。正如您所见，第一张图像没有图表，第二张图像没有形状，第三张图像没有条件格式。

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}

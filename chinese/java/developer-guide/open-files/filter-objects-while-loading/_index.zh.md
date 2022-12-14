---
title: 加载工作簿或工作表时过滤对象
type: docs
weight: 1060
url: /zh/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **可能的使用场景**
请用[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter)从工作簿中筛选数据时的属性。但是如果你想从单个工作表中过滤数据，那么你将不得不覆盖[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ） 方法。请提供来自[加载数据过滤器选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)创建或使用时的枚举[加载过滤器](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

这[加载数据过滤器选项](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)枚举具有以下值。

- [没有任何](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [全部](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING 单元格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [单元错误](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [公式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [细胞数据](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [图表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [形状](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [合并区域](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [条件格式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [数据验证](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [数据透视表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [桌子](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [超级链接](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [SHEET_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [SHEET_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [BOOK_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [设置](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_地图](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [结构体](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [文件属性](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [风格](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **加载工作簿时筛选对象**
以下示例代码说明了如何从工作簿中筛选图表。请检查[示例 excel 文件](5472489.xlsx)用于此代码和[输出PDF](5472488.pdf)由它产生。正如您在输出 PDF 中看到的那样，所有图表都已从工作簿中过滤掉。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **加载工作表时过滤对象**
下面的示例代码加载[源文件](5472492.xlsx)并使用自定义过滤器从其工作表中过滤以下数据。

- 它从名为 NoCharts 的工作表中过滤图表。
- 它从名为 NoShapes 的工作表中过滤形状。
- 它从名为 NoConditionalFormatting 的工作表中过滤条件格式。

一次，它加载[源文件](5472492.xlsx)使用自定义过滤器，它会一张一张地拍摄所有工作表的图像。这是供您参考的输出图像。如您所见，第一张图片没有图表，第二张图片没有形状，第三张图片没有条件格式。

- [无图表.png](5472493.png)
- [无形.png](5472491.png)
- [无条件格式.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}

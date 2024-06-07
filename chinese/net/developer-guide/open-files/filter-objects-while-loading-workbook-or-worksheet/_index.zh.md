---
title: 加载工作簿或工作表时筛选对象
type: docs
weight: 330
url: /zh/net/filter-objects-while-loading-workbook-or-worksheet/
---

## **可能的使用场景**
在从工作簿中筛选数据时，请使用[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)属性。但如果要从单独的工作表中筛选数据，则必须重写[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)方法。在创建或处理[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)时，请从[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)枚举中提供适当的值。

[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)枚举具有以下可能的值。

- 所有
- 工作簿设置
- 空单元格
- 单元格布尔值
- 单元格数据
- 单元格错误
- 单元格数值
- 单元格字符
- 单元格数值
- Chart
- 条件格式
- 数据验证
- 已定义名称
- 文档属性
- 公式
- 超链接
- 合并区域
- 透视表
- 设置
- 形状
- 工作表数据
- 工作表设置
- 结构
- 样式
- 表格
- VBA
- Xml映射
## **在加载工作簿时过滤对象**
以下示例代码说明如何从工作簿中过滤图表。请查看本代码中使用的[示例Excel文件](5115258.xlsx)和由此生成的[输出PDF](5115257.pdf)。如您在输出PDF中所见，所有图表均已从工作簿中过滤。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **在加载工作表时过滤对象**
以下示例代码加载源Excel文件并使用自定义过滤器从其工作表中筛选以下数据。

- 从名为NoCharts的工作表中筛选图表。
- 从名为NoShapes的工作表中筛选形状。
- 从名为NoConditionalFormatting的工作表中筛选条件格式。

一旦使用自定义过滤器加载源Excel文件，会逐个获取所有工作表的图片。以下是供参考的输出图片。正如您所看到的，第一张图片没有图表，第二张图片没有形状，第三张图片没有条件格式。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


根据工作表名称使用CustomLoadFilter类的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}

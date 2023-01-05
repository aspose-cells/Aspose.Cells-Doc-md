---
title: 加载工作簿或工作表时过滤对象
type: docs
weight: 330
url: /zh/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **可能的使用场景**
请用[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)从工作簿中筛选数据时的属性。但是如果你想从单个工作表中过滤数据，那么你将不得不覆盖[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)方法。请提供适当的值[加载数据过滤器选项](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)创建或使用时的枚举[加载过滤器](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

这[加载数据过滤器选项](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)枚举具有以下可能的值。

- 全部
- 书籍设置
- 细胞空白
- 单元布尔
- 细胞数据
- 细胞错误
- 细胞数值
- 单元串
- 细胞价值
- 图表
- 条件格式
- 数据验证
- 定义名称
- 文档属性
- 公式
- 超级链接
- 合并区
- 数据透视表
- 设置
- 形状
- 表数据
- 图纸设置
- 结构
- 风格
- 桌子
- VBA
- XML地图
## **加载工作簿时过滤对象**
以下示例代码说明了如何从工作簿中筛选图表。请检查[示例 excel 文件](5115258.xlsx)用于此代码和[输出 PDF](5115257.pdf)由它产生。正如您在输出 PDF 中看到的那样，所有图表都已从工作簿中过滤掉。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **加载工作表时过滤对象**
下面的示例代码加载[源文件](5115255.xlsx)并使用自定义过滤器从其工作表中过滤以下数据。

- 它从名为 NoCharts 的工作表中过滤图表。
- 它从名为 NoShapes 的工作表中过滤形状。
- 它从名为 NoConditionalFormatting 的工作表中过滤条件格式。

一次，它加载[源文件](5115255.xlsx)使用自定义过滤器，它会一张一张地拍摄所有工作表的图像。这是供您参考的输出图像。如您所见，第一张图片没有图表，第二张图片没有形状，第三张图片没有条件格式。

- [无图表.png](5115254.png)
- [无形.png](5115256.png)
- [无条件格式.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


这是根据工作表名称使用 CustomLoadFilter 类的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}

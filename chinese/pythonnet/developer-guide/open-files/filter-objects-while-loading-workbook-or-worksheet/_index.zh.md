---
title: 在加载工作簿或工作表时过滤对象
type: docs
weight: 330
url: /zh/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **可能的使用场景**
在从工作簿中过滤数据时，请使用 [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) 属性。如果想要过滤单个工作表中的数据，则需要覆盖 [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet) 方法。在创建或使用 [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) 时，请提供适当的 [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) 枚举值。

[LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) 枚举具有以下可能值。

- 所有
- 文档设置
- 单元格空白
- 单元格布尔
- 单元格数据
- 单元格错误
- 单元格数值
- 单元格字符串
- 单元格值
- Chart
- 条件格式
- 数据验证
- 定义名称
- 文档属性
- 公式
- 超链接
- 合并区域
- 数据透视表
- 设置
- 形状
- 表单数据
- 表格设置
- 结构
- 样式
- 表
- VBA
- Xml映射
## **加载工作簿时过滤对象**
以下示例代码说明了如何从工作簿中筛选图表。请查看此代码中使用的[示例excel文件](5115258.xlsx)和由此生成的[输出PDF](5115257.pdf)。从输出PDF中可以看出，所有图表都已从工作簿中筛选出。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

{{< app/cells/assistant language="python-net" >}}

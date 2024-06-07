---
title: 在GridDesktop中加载工作簿时过滤对象
type: docs
weight: 1060
url: /zh/net/aspose-cells-griddesktop/loading-filter
description: This article describes how to use loading filter in GridDesktop.
keywords: GridDesktop，正在加载，正在加载筛选器，筛选器
---

## **可能的使用场景**
在从工作簿中筛选数据时，请使用[GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)属性。

[GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions)枚举具有以下值。
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
## **在加载工作簿时过滤数据**
以下示例代码演示了在工作簿中筛选绘图的方法。请参考[示例Excel文件](5472489.xlsx)。如你所见，工作簿中的所有图表/形状/图像都被过滤掉了。
![没有图像的工作簿](nodrawing.png)
### **示例代码**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}


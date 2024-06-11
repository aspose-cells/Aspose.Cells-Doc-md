---
title: 在GridDesktop中加载工作簿时过滤对象
type: docs
weight: 1060
url: /zh/net/aspose-cells-griddesktop/loading-filter
description: 本文介绍了如何在GridDesktop中使用加载过滤器。
keywords: GridDesktop,loading,loading filter,filter
---

## **可能的使用场景**
在从工作簿筛选数据时，请使用[GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)属性。

[GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions)枚举具有以下值。
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
## **在加载工作簿时过滤数据**
以下示例代码说明了如何过滤工作薄中的图纸。请查看 [示例 excel 文件](5472489.xlsx)。如您所见，工作簿中的所有图表/形状/图像都已被过滤掉。
![无图工作薄](nodrawing.png)
### **示例代码**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}


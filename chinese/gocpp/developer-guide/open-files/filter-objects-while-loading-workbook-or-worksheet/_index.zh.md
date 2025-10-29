---
title: 在加载工作簿或工作表时过滤对象，使用Golang via C++
linktitle: 在加载工作簿或工作表时过滤对象
type: docs
weight: 330
url: /zh/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: 学习如何在使用 Aspose.Cells for C++ 加载工作簿或工作表时过滤图表、形状和条件格式等对象。
---

## **可能的使用场景**
在从工作簿中过滤数据时，请使用[LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/)属性。如果要从单个工作表中过滤数据，则必须重写[LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/)方法。在创建或使用[LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/)时，请提供适当的[LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)枚举值。

[LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/)枚举具有以下可能值。

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **加载工作表时过滤对象**
以下示例代码加载了[源excel文件](5115255.xlsx)，并使用自定义过滤器从其工作表中筛选以下数据。

- 它会从名为NoCharts的工作表中筛选图表。
- 它会从名为NoShapes的工作表中筛选形状。
- 它会从名为NoConditionalFormatting的工作表中筛选条件格式。

一旦使用自定义过滤器加载了[源excel文件](5115255.xlsx)，它会逐个工作表地获取所有工作表的图像。以下是用于参考的输出图像。可以看出，第一张图像没有图表，第二张图像没有形状，第三张图像没有条件格式。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
这是如何根据工作表名称使用CustomLoadFilter类。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}

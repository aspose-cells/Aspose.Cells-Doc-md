---
title: 表格和范围
type: docs
weight: 30
url: /zh/cpp/tables-and-ranges/
---
## **介绍**
有时您在 Microsoft Excel 中创建了一个表格，并且不想继续使用它附带的表格功能。相反，您想要看起来像桌子的东西。要在不丢失格式的情况下保留表格中的数据，请将表格转换为常规范围的数据。 Aspose.Cells 不支持表和列表对象的 Microsoft Excel 的此功能。
## **使用 Microsoft Excel**
使用**转换为范围**在不丢失格式的情况下快速将表格转换为范围的功能。在 Microsoft Excel 2007/2010 中：

1. 单击表格中的任意位置以确保活动单元格位于表格列中。
1. 在**设计**选项卡，在**工具**分组，点击**转换为范围**.

{{% alert color="primary" %}} 

表格转换为区域后，表格功能将不再可用。例如，行标题不再包含排序和筛选箭头，公式中使用的结构化引用（使用表名的引用）变成了常规单元格引用。

{{% /alert %}} 
## **使用 Aspose.Cells**
以下代码片段使用 Aspose.Cells 演示了相同的功能。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange.cpp" >}}

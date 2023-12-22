---
title: 表格和范围
type: docs
weight: 30
url: /zh/cpp/tables-and-ranges/
---
##  **介绍**
有时，您在 Microsoft Excel 中创建了一个表格，但不想继续使用它附带的表格功能。相反，您想要看起来像桌子的东西。要保留表中的数据而不丢失格式，请将表转换为常规数据范围。 Aspose.Cells 确实支持 Microsoft Excel 表和列表对象的此功能。
##  **使用 Microsoft Excel**
使用**转换为范围**功能可快速将表格转换为范围而不丢失格式。在 Microsoft Excel 2007/2010 中：

1. 单击表中的任意位置以确保活动单元格位于表列中。
1. 上**设计**选项卡，在**工具**组，单击*转换为范围**。

{{% alert color="primary" %}} 

表转换为范围后，表功能不再可用。例如，行标题不再包含排序和筛选箭头，公式中使用的结构化引用（使用表名称的引用）变为常规单元格引用。

{{% /alert %}} 
##  **使用Aspose.Cells**
以下代码片段使用 Aspose.Cells 演示了相同的功能。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}

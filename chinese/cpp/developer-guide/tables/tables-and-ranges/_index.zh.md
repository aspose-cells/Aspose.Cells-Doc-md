---
title: 表格和范围
type: docs
weight: 30
url: /zh/cpp/tables-and-ranges/
---

## **介绍**
有时，在Microsoft Excel中创建表格后，您不想继续使用它提供的表格功能。相反，您想要看起来像表格的东西。要保留表格中的数据而又不丢失格式，请将表格转换为普通数据范围。Aspose.Cells支持Microsoft Excel中表格和列表对象的此功能。
## **使用Microsoft Excel**
使用 **转换为范围** 功能快速将表格转换为范围，而不会丢失格式。在Microsoft Excel 2007/2010中：

1. 单击表格中的任何位置，确保活动单元格位于表格列中。
1. 在 **设计** 标签中，单击 **工具** 组中的 **转换为范围**。

{{% alert color="primary" %}} 

表格转换为范围后，表格功能将不再可用。例如，行标题不再包括排序和过滤箭头，以及在公式中使用的结构引用（使用表名的引用）将变为常规单元格引用。

{{% /alert %}} 
## **使用Aspose.Cells**
以下代码片段展示了使用Aspose.Cells实现相同功能的方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}

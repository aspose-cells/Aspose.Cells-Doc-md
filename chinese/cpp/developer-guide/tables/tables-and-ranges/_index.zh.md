---
title: 表格和范围
type: docs
weight: 30
url: /zh/cpp/tables-and-ranges/
---

## **介绍**
有时您在Microsoft Excel中创建一个表格，却不想继续使用该表格的功能。相反，您可能希望看起来像表格的样子。为了保留表格中的数据而不丢失格式，将表格转换为常规数据范围。Aspose.Cells确实支持Microsoft Excel的表格和列表对象的此功能。
## **使用Microsoft Excel**
使用**转换为范围**功能快速将表格转换为常规数据范围，而不丢失格式。在Microsoft Excel 2007/2010中：

1. 单击表中的任意位置，确保活动单元格位于表列中。
1. 在**设计**选项卡的**工具**组中，单击**转换为范围**。

{{% alert color="primary" %}} 

表格在转换为范围后将不再可用其表格功能。例如，行标头不再包含排序和筛选箭头，以及在公式中使用的结构引用（使用表名称的引用）会变成常规单元格引用。

{{% /alert %}} 
## **使用Aspose.Cells**
以下代码片段演示了使用Aspose.Cells实现相同功能。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}

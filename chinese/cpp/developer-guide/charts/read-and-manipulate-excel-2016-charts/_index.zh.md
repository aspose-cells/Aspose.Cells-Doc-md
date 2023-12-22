---
title: 阅读和操作 Excel 2016 图表
type: docs
weight: 20
url: /zh/cpp/read-and-manipulate-excel-2016-charts/
---
##  **可能的使用场景**
Aspose.Cells 支持读取和操作 Microsoft Excel 2016 图表，这些图表在 Microsoft Excel 2013 或更早版本中不存在。
##  **阅读和操作 Excel 2016 图表**
以下示例代码加载[Excel 文件示例](66519072.xlsx)其中第一个工作表中包含 Excel 2016 图表。它一一读取所有图表，并根据图表类型更改其标题。以下屏幕截图显示了执行代码之前的示例 Excel 文件。正如您所看到的，所有图表的图表标题都是相同的。

![待办事项：图像_替代_文本](read-and-manipulate-excel-2016-charts_1.png)

下面的屏幕截图显示了[输出Excel文件](66519073.xlsx)执行代码后。如您所见，图表标题根据其图表类型进行更改。

![待办事项：图像_替代_文本](read-and-manipulate-excel-2016-charts_2.png)
##  **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-ReadAndManipulateExcel2016Charts-new.cpp" >}}
##  **控制台输出**
以下是使用提供的示例 Excel 文件执行上述示例代码时的控制台输出。

{{< highlight "java" >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}

---
title: 读取和操作 Excel 2016 图表
type: docs
weight: 20
url: /zh/cpp/read-and-manipulate-excel-2016-charts/
---
## **可能的使用场景**
Aspose.Cells 支持读取和操作 Microsoft Excel 2016 图表，这些图表在 Microsoft Excel 2013 或更早版本中不存在。
## **读取和操作 Excel 2016 图表**
下面的示例代码加载[示例 Excel 文件](66519072.xlsx)其中包含第一个工作表中的 Excel 2016 图表。它会一张一张地读取所有图表，并根据图表类型更改其标题。以下屏幕截图显示了代码执行前的示例 Excel 文件。如您所见，所有图表的图表标题都相同。

![待办事项：图像_替代_文本](read-and-manipulate-excel-2016-charts_1.png)

以下屏幕截图显示了[输出Excel文件](66519073.xlsx)代码执行后。如您所见，图表标题根据其图表类型进行了更改。

![待办事项：图像_替代_文本](read-and-manipulate-excel-2016-charts_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-ReadAndManipulateExcel2016Charts.cpp" >}}
## **控制台输出**
这是使用提供的示例 Excel 文件执行时上述示例代码的控制台输出。

{{< highlight "java" >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}

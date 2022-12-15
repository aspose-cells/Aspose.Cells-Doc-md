---
title: 读取和操作 Excel 2016 图表
type: docs
weight: 48
url: /zh/net/read-and-manipulate-excel-2016-charts/
---
## **可能的使用场景**
Aspose.Cells 现在支持读取和操作 Microsoft Excel 2016 图表，这些图表在 Microsoft Excel 2013 或更早版本中不存在。
## **读取和操作 Excel 2016 图表**
下面的示例代码加载[源文件](22774101.xlsx)其中包含第一个工作表中的 Excel 2016 图表。它会一张一张地读取所有图表，并根据图表类型更改其标题。以下屏幕截图显示了代码执行前的源 excel 文件。如您所见，所有图表的图表标题都相同。

![待办事项：图像_替代_文本](read-and-manipulate-excel-2016-charts_1.png)

以下屏幕截图显示了[输出excel文件](22774104.xlsx)代码执行后。如您所见，图表标题根据其图表类型进行了更改。

![待办事项：图像_替代_文本](read-and-manipulate-excel-2016-charts_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-ReadAndManipulateExcel2016Charts.cs" >}}
## **控制台输出**
这是使用提供的执行时上述示例代码的控制台输出[源文件](22774101.xlsx).

{{< highlight "java" >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}


## **推进主题**
- [创建瀑布图](/cells/zh/net/creating-waterfall-chart/)

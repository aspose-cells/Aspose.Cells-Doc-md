---
title: 读取和操作 Excel 2016 图表
type: docs
weight: 20
url: /zh/cpp/read-and-manipulate-excel-2016-charts/
---

## **可能的使用场景**
Aspose.Cells 支持读取和操作 Microsoft Excel 2016 图表，这些图表在 Microsoft Excel 2013 或更早版本中不存在。
## **读取和操作 Excel 2016 图表**
以下示例代码加载了包含Excel 2016图表的样本Excel文件。它逐个读取所有图表，并根据其图表类型更改其标题。下面的屏幕截图显示了代码执行之前的样本Excel文件。正如您所见，所有图表的标题都是相同的。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

下面的屏幕截图显示了代码执行后的[输出Excel文件](66519073.xlsx)。正如您所见，每个图表的标题都改变成了其图表类型。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-ReadAndManipulateExcel2016Charts-new.cpp" >}}
## **控制台输出**
上述示例代码在提供的示例Excel文件上执行时的控制台输出如下。

{{< highlight java >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}

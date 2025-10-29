---
title: 读取和操作Excel 2016图表
type: docs
weight: 20
url: /zh/cpp/read-and-manipulate-excel-2016-charts/
---

## **可能的使用场景**
Aspose.Cells支持读取和操作Microsoft Excel 2016图表，这些图表在Microsoft Excel 2013或更早版本中不存在。
## **读取和操作Excel 2016图表**
以下示例代码加载了包含Excel 2016图表的 [示例Excel文件](66519072.xlsx) 在第一个工作表中。它逐个读取所有图表并根据图表类型更改其标题。以下截图显示了执行代码之前的示例Excel文件。您可以看到，所有图表的标题都是相同的。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

以下截图显示了代码执行后的 [输出Excel文件](66519073.xlsx)。您可以看到，图表的标题已根据其图表类型更改。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-ReadAndManipulateExcel2016Charts-new.cpp" >}}
## **控制台输出**
这是上述示例代码在提供的示例Excel文件上执行时的控制台输出。

{{< highlight java >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}

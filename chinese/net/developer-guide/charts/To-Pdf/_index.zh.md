---
title: 图表转换为PDF 
description: 学习如何使用 Aspose.Cells for .NET 将图表转换为 PDF 文档。我们的指南将演示如何从 Microsoft Excel 导出图表并将其保存为 PDF 以供进一步分发和存档。
keywords: Aspose.Cells for .NET，图表转 PDF，Microsoft Excel，PDF 转换，导出，分发，存档。
type: docs
weight: 47
url: /zh/net/chart-to-pdf/
---

## **将图表渲染为PDF**

为了将图表渲染为PDF格式，Aspose.Cells API已公开了[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)方法，能够将结果PDF存储在磁盘路径或流中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **使用所需的页面大小创建图表PDF**
您可以使用Aspose.Cells创建所需页面大小的图表PDF，并指定您希望如何在页面内对齐图表，如顶部、底部、中心、左侧、右侧等。此外，输出图表可以以流或磁盘形式创建。请参阅以下示例代码，该代码加载了[示例Excel文件](64716906.xlsx)，访问工作表中的第一个图表，然后将其转换为[输出PDF](64716907.pdf)并指定所需的页面大小。以下截图显示，输出PDF中的页面大小为7x7，如代码内指定的，且图表在水平和垂直方向上都居中对齐。 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}


---
title: 转换为PDF 
description: 学习如何使用Aspose.Cells for .NET将图表转换为PDF文档。我们的指南将演示如何从Microsoft Excel中导出图表并保存为PDF以便进一步分发和存档。
keywords: Aspose.Cells for .NET, 图表转PDF, Microsoft Excel, PDF转换, 导出, 分发, 存档。
type: docs
weight: 47
url: /zh/net/chart-to-pdf/
---

## **渲染图表为PDF**

为了将图表呈现为PDF格式，Aspose.Cells API已暴露了[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)方法，可将生成的PDF存储在磁盘路径或流上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **使用所需的页面大小创建图表PDF**
您可以使用Aspose.Cells创建所需页面大小的图表PDF，并指定希望如何在页面内对齐图表，例如顶部、底部、中心、左侧、右侧等。此外，输出的图表可在流中或磁盘上创建。请参阅以下示例代码，加载[示例Excel文件](64716906.xlsx)，访问工作表中的第一个图表，然后根据需求页面大小将其转换为[输出PDF](64716907.pdf)。下面的屏幕截图显示输出PDF中所指定的页面大小为7x7，且图表在水平和垂直方向上均居中。 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}


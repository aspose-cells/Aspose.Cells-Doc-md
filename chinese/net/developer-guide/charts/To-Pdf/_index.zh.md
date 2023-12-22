---
title: 图表至PDF
description: 了解如何使用 Aspose.Cells for .NET 将图表转换为 PDF 文档。我们的指南将演示如何从 Microsoft Excel 导出图表并将其另存为 PDF 以供进一步分发和存档。
keywords: Aspose.Cells for .NET, Chart to PDF, Microsoft Excel, PDF Conversion, Export, Distribution, Archiving.
type: docs
weight: 47
url: /zh/net/chart-to-pdf/
---
##  **渲染图至PDF**

为了将图表呈现为 PDF 格式，Aspose.Cells API 公开了[**图表.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)方法能够将结果 PDF 存储在光盘路径或流上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

##  **使用所需的页面大小创建图表 PDF**
您可以使用 Aspose.Cells 创建具有所需页面大小的图表 Pdf，并指定如何在页面内对齐图表，如顶部、底部、中心、左侧、右侧等。此外，输出图表可以在流中或在磁盘上创建。请参阅以下加载示例代码[Excel 文件示例](64716906.xlsx)，访问工作表中的第一个图表，然后将其转换为[输出PDF](64716907.pdf)与所需的页面大小。以下屏幕截图显示输出 Pdf 中的页面大小为代码内指定的 7x7，并且图表水平和垂直居中对齐。

![待办事项：图像_替代_文本](create-chart-pdf-with-desired-page-size_1.png)
##  **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}


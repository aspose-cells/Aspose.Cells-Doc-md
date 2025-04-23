---
title: 图表转换为PDF 
description: 学习如何使用 Aspose.Cells for Python via .NET 将图表转换为 PDF 文档。我们的指南将演示如何导出 Microsoft Excel 中的图表，并将其保存为 PDF 以便进一步分发和存档。
keywords: Aspose.Cells for Python via .NET，图表转PDF，Microsoft Excel，PDF转换，导出，分发，归档。
type: docs
weight: 47
url: /zh/python-net/chart-to-pdf/
---

## **将图表渲染为PDF**

为了将图表渲染为PDF格式，Aspose.Cells for Python via .NET API已经暴露了[**Chart.to_pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_pdf)方法，能够将生成的PDF存储在硬盘路径或流中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRenderingChartToPDF.py" >}}

## **使用所需的页面大小创建图表PDF**
你可以使用Aspose.Cells for Python via .NET创建具有所需页面尺寸的图表PDF，并指定图表在页面内的对齐方式，如顶部、底部、居中、左、右等。此外，输出的图表可以在流中或在磁盘上创建。请查看以下示例代码，该代码加载[示例Excel文件](64716906.xlsx)，访问工作表中的第一个图表，然后以所需页面尺寸将其转换为[输出Pdf](64716907.pdf)。下面的截图显示输出Pdf中的页面尺寸为代码中指定的7x7，图表水平和垂直居中对齐。 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateChartPDFWithDesiredPageSize.py" >}}


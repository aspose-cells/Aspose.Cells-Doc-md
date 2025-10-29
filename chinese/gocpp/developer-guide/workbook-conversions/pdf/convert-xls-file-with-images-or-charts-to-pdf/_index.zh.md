---
title: 将包含图像或图表的 XLS 文件转换为 PDF，使用 Golang 通过 C++
linktitle: 将带有图像或图表的XLS文件转换为PDF
type: docs
weight: 50
url: /zh/go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: 使用 Aspose.Cells 通过 C++ 将包含图像或图表的 XLS 文件转换为 PDF 文档，使用 Golang。
---

{{% alert color="primary" %}} 

Aspose.Cells支持将包含图片和图表的XLS文件转换为PDF文档。Aspose.Cells for C++可以独立完成将电子表格转换为PDF的任务：不需要Aspose.PDF for C++。此过程可以在内存中完成，因为不依赖临时或中间XML文件。这意味着大文件（如含有图片、图表及其他绘图对象的Excel）可以快速高效地转换。

{{% /alert %}} 
## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

如果电子表格包含公式，最好在渲染为 PDF 之前调用 [Calculate(CalculationData data)](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) 方法。这可以确保重新计算依赖公式的值，并在 PDF 中渲染正确的数值。

{{% /alert %}}

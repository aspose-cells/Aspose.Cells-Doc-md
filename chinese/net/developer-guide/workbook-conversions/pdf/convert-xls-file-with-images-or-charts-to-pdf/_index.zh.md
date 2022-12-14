---
title: 将带有图像或图表的 XLS 文件转换为 PDF
type: docs
weight: 50
url: /zh/net/convert-xls-file-with-images-or-charts-to-pdf/
---
{{% alert color="primary" %}} 

Aspose.Cells 支持将包含图像和图表的 XLS 文件转换为 PDF 文档。 Aspose.Cells for .NET 可以独立工作将电子表格转换为PDF： Aspose.PDF for .NET 不需要转换。该过程可以在内存中完成，因为该过程不依赖于临时或中间 XML 文件。这意味着可以快速高效地转换大型 Excel 文件，例如包含图像、图表和其他绘图对象的文件。

{{% /alert %}} 
## **示例代码**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

如果电子表格包含公式，最好调用[工作簿.计算公式](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)在呈现为 PDF 之前的方法。这样做可确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

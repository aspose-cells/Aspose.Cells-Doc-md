---
title: 将带有图像或图表的XLS文件转换为PDF
type: docs
weight: 50
url: /zh/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells支持将包含图像和图表的XLS文件转换为PDF文档。Aspose.Cells for .NET可以独立地工作，将电子表格转换为PDF，无需使用Aspose.PDF for .NET进行转换。该过程可以在内存中完成，不依赖于临时或中间XML文件。这意味着可以快速高效地转换大型Excel文件，例如包含图像、图表和其他绘图对象的文件。

{{% /alert %}} 
## **示例代码**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

如果电子表格中包含公式，最好在呈现到PDF之前调用 [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) 方法。这样做可以确保基于公式的值被重新计算，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

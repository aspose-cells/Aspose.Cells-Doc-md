---
title: 将带有图片或图表的XLS文件转换为PDF
type: docs
weight: 50
url: /zh/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells支持将包含图像和图表的XLS文件转换为PDF文档。Aspose.Cells for .NET可以独立工作，将电子表格转换为PDF：不需要Aspose.PDF for .NET进行转换。该过程可以在内存中完成，因为该过程不依赖于临时或中间XML文件。这意味着大型Excel文件，例如包含图片、图表和其他绘图对象的文件，可以快速高效地转换。

{{% /alert %}} 
## **示例代码**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

如果电子表格包含公式，最好在渲染到PDF之前调用[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)方法。这样做确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

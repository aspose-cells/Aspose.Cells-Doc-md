---
title: 将每个工作表保存为单独的 PDF 文件
type: docs
weight: 130
url: /zh/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells 支持将包含图像、图表等的 XLS 文件转换为 PDF 文档。Aspose.Cells for .NET 可以独立工作，将电子表格转换为 PDF，无需使用 Aspose.PDF for .NET 进行转换。此转换不需要创建任何临时文件，整个过程可以在内存中完成。

{{% /alert %}} 
## **将每个工作表保存为不同的PDF文件**
如果您需要将模板 Excel 文件中的每个工作表保存为不同的 PDF 文件，您可以轻松实现。您可以尝试逐个将一个工作表索引设置为 **[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** 选项，以便呈现为 PDF。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为 PDF 格式之前调用 [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做可以确保重新计算公式依赖的值，并在 PDF 中呈现正确的值。

{{% /alert %}}

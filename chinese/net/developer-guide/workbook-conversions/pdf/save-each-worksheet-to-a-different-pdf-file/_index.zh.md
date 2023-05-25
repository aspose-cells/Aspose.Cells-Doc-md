---
title: 将每个工作表保存到不同的 PDF 文件
type: docs
weight: 130
url: /zh/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells 支持将 XLS 文件（包含图像、图表等）转换为 PDF 文档。 Aspose.Cells for .NET 可以独立工作，将电子表格转换为 PDF，您不需要使用 Aspose.PDF for .NET 进行转换。转换不需要软件创建或使用任何临时文件，因为整个过程可以在内存中完成。

{{% /alert %}} 
##  **将每个工作表保存到不同的 PDF 文件**
如果您需要将每个工作表保存在模板 Excel 文件中以生成不同的 PDF 文件，您可以轻松实现。您可以尝试将一张纸索引设置为**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**一次渲染到 PDF 的选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好调用[工作簿.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)就在将电子表格呈现为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

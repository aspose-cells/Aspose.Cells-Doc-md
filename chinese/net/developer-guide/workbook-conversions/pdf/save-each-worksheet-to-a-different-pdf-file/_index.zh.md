---
title: 将每个工作表保存为不同的PDF文件
type: docs
weight: 130
url: /zh/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells支持将包含图像、图表等的XLS文件转换为PDF文档。Aspose.Cells for .NET可以独立地工作，将电子表格转换为PDF，无需使用Aspose.PDF for .NET进行转换。转换不需要软件创建或使用任何临时文件，整个过程可以在内存中完成。

{{% /alert %}} 
## **将每个工作表保存为不同的PDF文件**
如果您需要保存模板 Excel 文件中的每个工作表以生成不同的 PDF 文件，这很容易实现。您可以尝试逐个将一个工作表索引设置为 [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) 选项以渲染为 PDF。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

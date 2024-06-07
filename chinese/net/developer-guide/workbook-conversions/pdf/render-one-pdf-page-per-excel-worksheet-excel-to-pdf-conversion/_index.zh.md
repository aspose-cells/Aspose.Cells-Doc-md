---
title: 每个Excel工作表呈现为一个PDF页面 - Excel转PDF转换
type: docs
weight: 100
url: /zh/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

当处理大型 Microsoft Excel 文件时（例如一个包含许多工作表，每个工作表有50列和300行或更多数据的工作簿），您可能希望 PDF 输出显示每个工作表的一页，而不管工作表的大小如何。这意味着每个页面可能具有完全不同的页面大小。可以通过使用 Aspose.Cells for .NET 来实现。

{{% /alert %}} 

请参阅以下转换多个工作表的 Excel 文件为 PDF 的示例代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

如果将 [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) 选项设置为 **true**，则将渲染所有工作表内容到一个 PDF 页。

{{% /alert %}} {{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为 PDF 之前调用 [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样可以确保重新计算公式依赖的值，并在 PDF 中呈现正确的值。

{{% /alert %}}

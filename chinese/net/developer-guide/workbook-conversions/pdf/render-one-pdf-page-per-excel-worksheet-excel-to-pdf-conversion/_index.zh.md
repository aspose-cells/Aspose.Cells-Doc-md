---
title: 每个 Excel 工作表渲染一个 PDF 页 - Excel 到 PDF 的转换
type: docs
weight: 100
url: /zh/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

处理大型 Microsoft Excel 文件时（例如，工作簿有很多工作表，每个工作表有 50 列和 300 行或更多行数据），您可能希望 PDF 输出显示每个工作表一页，而不管工作表的大小.这意味着每个页面可能具有完全不同的页面大小。这可以通过使用 Aspose.Cells for .NET 来实现。

{{% /alert %}} 

请参阅以下将包含多个工作表的 Excel 文件转换为 PDF 的示例代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

如果[每张一页](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet)选项设置为**真的**，所有工作表内容将呈现为一个 PDF 页面。

{{% /alert %}} {{% alert color="primary" %}} 

如果您的电子表格包含公式，最好调用[工作簿.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)就在将电子表格呈现为 PDF 之前。这可确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

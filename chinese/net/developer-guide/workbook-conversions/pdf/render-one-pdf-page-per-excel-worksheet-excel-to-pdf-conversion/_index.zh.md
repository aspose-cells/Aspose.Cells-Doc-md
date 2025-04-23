---
title: 将Excel工作表渲染为一份PDF页面  Excel转PDF转换
type: docs
weight: 100
url: /zh/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

当处理大型Microsoft Excel文件（例如具有许多工作表，每个工作表有50列和300多行数据）时，您可能希望PDF输出每个工作表显示一页，而不考虑工作表的大小。这意味着每一页可能具有截然不同的页面大小。这可以通过使用Aspose.Cells for .NET来实现。

{{% /alert %}} 

请查看以下示例代码，将多个工作表的Excel文件转换为PDF。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

如果[OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet)选项设置为**true**，则所有工作表内容将呈现为一个PDF页面。

{{% /alert %}} {{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为PDF之前调用[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这将确保重新计算公式相关值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

---
title: 限制生成的页数 - Excel 到 PDF 的转换
type: docs
weight: 180
url: /zh/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

有时，您希望将一系列页面打印到输出 PDF 文件中。 Aspose.Cells 能够设置将 Excel 电子表格转换为 PDF 文件格式时生成多少页的限制。

{{% /alert %}}

## **限制生成的页数**

以下示例显示如何将 Microsoft Excel 文件中的一系列页面（3 和 4）呈现为 PDF。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[**工作簿.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)就在将其呈现为 PDF 之前。这样做可确保重新计算与公式相关的值，并在输出文件中呈现正确的值。

{{% /alert %}}

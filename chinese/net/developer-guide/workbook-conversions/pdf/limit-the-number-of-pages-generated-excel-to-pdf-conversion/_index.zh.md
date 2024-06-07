---
title: 限制生成的页面数量 - Excel转PDF转换
type: docs
weight: 180
url: /zh/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

有时，您希望打印一系列页面到输出PDF文件中。Aspose.Cells 能够在将Excel电子表格转换为PDF文件格式时设置生成的页面数量上限。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示如何将 Microsoft Excel 文件的页面范围(第3页和第4页)渲染为PDF。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

如果电子表格中包含公式，最好在将其渲染为PDF之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做可以确保重新计算公式相关的值，并在输出文件中呈现正确的值。

{{% /alert %}}

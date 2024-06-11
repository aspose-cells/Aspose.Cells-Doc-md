---
title: 限制生成的页面数量 - 将Excel转换为PDF
type: docs
weight: 180
url: /zh/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

有时，您希望将某个范围的页面打印到输出PDF文件中。Aspose.Cells可以在将Excel电子表格转换为PDF文件格式时设置生成的页面数量限制。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示了如何将Microsoft Excel文件的页面范围（第3页和第4页）呈现为PDF。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

如果电子表格中包含公式，最好在将其呈现为PDF文件之前调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样可以确保重新计算公式相关值，并在输出文件中呈现正确的值。

{{% /alert %}}

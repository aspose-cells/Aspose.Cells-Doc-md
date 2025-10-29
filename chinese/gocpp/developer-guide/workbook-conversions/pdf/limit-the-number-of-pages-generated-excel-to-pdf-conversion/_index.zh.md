---
title: 限制生成的页数——使用 C++ 通过 Golang 将 Excel 转换为 PDF
linktitle: 限制生成页面的数量
type: docs
weight: 180
url: /zh/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: 学习如何在使用 C++ 通过 Golang 使用 Aspose.Cells 转换 Excel 为 PDF 时限制生成的页数。
---

{{% alert color="primary" %}}

有时，您希望将某个范围的页面打印到输出PDF文件中。Aspose.Cells可以在将Excel电子表格转换为PDF文件格式时设置生成的页面数量限制。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示了如何将Microsoft Excel文件的页面范围（第3页和第4页）呈现为PDF。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

如果电子表格中包含公式，最好在将其呈现为PDF文件之前调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)。这样可以确保重新计算公式相关值，并在输出文件中呈现正确的值。

{{% /alert %}}

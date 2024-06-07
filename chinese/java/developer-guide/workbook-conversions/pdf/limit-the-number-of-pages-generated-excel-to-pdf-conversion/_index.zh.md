---
title: 限制生成的页面数量 - Excel转PDF转换
type: docs
weight: 60
url: /zh/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

有时，您希望将一系列页面打印到输出 PDF 文件中。Aspose.Cells 具有在将 Excel 电子表格转换为 PDF 时设置生成页数限制的能力。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示如何将 Microsoft Excel 文件的页面范围(第3页和第4页)渲染为PDF。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其呈现为 PDF 格式之前调用 [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())。这样可以确保公式依赖值被重新计算，并在输出文件中呈现正确的值。

{{% /alert %}}

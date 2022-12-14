---
title: 限制生成的页数 - Excel 到 PDF 的转换
type: docs
weight: 60
url: /zh/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

有时，您想要将一系列页面打印到输出 PDF 文件。 Aspose.Cells 可以设置将 Excel 电子表格转换为 PDF 时生成多少页的限制。

{{% /alert %}}

## **限制生成的页数**

以下示例显示如何将 Microsoft Excel 文件中的一系列页面（3 和 4）呈现为 PDF。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[**工作簿.计算公式**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()就在将其呈现为 PDF 格式之前。这样做可确保重新计算公式相关值，并在输出文件中呈现正确的值。

{{% /alert %}}

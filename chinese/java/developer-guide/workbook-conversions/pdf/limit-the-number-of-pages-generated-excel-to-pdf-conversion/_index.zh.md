---
title: 限制生成的页面数量 - 将Excel转换为PDF
type: docs
weight: 60
url: /zh/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

有时，你想将页面范围打印到一个输出PDF文件。Aspose.Cells可以设置在将Excel电子表格转换为PDF时生成多少页的限制。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示了如何将Microsoft Excel文件的页面范围（第3页和第4页）呈现为PDF。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将其渲染为PDF格式之前调用[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()）方法。这样可以确保计算依赖于公式的值，并在输出文件中呈现正确的值。

{{% /alert %}}

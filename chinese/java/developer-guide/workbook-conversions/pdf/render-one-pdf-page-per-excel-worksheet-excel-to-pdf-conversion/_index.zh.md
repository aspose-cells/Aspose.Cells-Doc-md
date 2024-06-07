---
title: 每个Excel工作表呈现为一个PDF页面 - Excel转PDF转换
type: docs
weight: 40
url: /zh/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

当处理大型 Microsoft Excel 文件时（例如具有许多工作表的工作簿，每个工作表具有 50 列和 300 行或更多数据），您可能希望 PDF 输出在每个工作表中显示一页，而不考虑工作表的大小。这意味着每个页面很可能具有完全不同的页面大小。这可以通过使用 Aspose.Cells for Java 实现。

{{% /alert %}}

请参阅以下转换多个工作表的 Excel 文件为 PDF 的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

如果 [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) 选项设置为 **true**，则所有工作表内容将呈现到一个 PDF 页面。由 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) 设置的纸张大小无效，但使用 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) 设置的其他设置仍然有效。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为 PDF 时调用 [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) 方法。这将确保重新计算公式依赖值，并在 PDF 中呈现正确的值。

{{% /alert %}}

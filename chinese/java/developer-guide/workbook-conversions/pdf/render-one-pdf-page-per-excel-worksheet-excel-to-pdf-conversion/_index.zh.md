---
title: 将Excel工作表渲染为一份PDF页面 - Excel转PDF转换
type: docs
weight: 40
url: /zh/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

当处理大型Microsoft Excel文件（例如一个具有许多工作表的工作簿，每个工作表都有50列和300行或更多数据时），您可能希望PDF输出显示每个工作表一页，而不管工作表的大小如何。 这意味着每个页面很可能会有完全不同的页面大小。 使用 Aspose.Cells for Java 可以实现这一点。

{{% /alert %}}

请查看以下示例代码，将多个工作表的Excel文件转换为PDF。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

如果[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet)选项设置为**true**，则所有工作表内容都将呈现为一个PDF页面。由[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)设置的纸张大小无效，但由[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)设置的其他设置仍然生效。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF之前立即调用[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())方法。这可以确保计算公式相关值，并在PDF中呈现正确的值。

{{% /alert %}}

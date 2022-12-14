---
title: 每个 Excel 工作表渲染一个 PDF 页面 - Excel 到 PDF 的转换
type: docs
weight: 40
url: /zh/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

处理大型 Microsoft Excel 文件时（例如，有许多工作表的工作簿，每个工作表有 50 列和 300 或更多行数据），您可能希望 PDF 输出显示每个工作表一页，而不管工作表的大小.这意味着每个页面可能具有完全不同的页面大小。这可以通过使用 Aspose.Cells for Java 来实现。

{{% /alert %}}

请参阅以下将包含多个工作表的 Excel 文件转换为 PDF 的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

如果[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet)选项设置为**真的**，所有工作表内容都呈现为一个 PDF 页面。纸张尺寸由[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)无效，但其他设置设置为[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)仍然生效。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好调用[**工作簿.计算公式**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()方法就在将电子表格呈现为 PDF 之前。这可确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

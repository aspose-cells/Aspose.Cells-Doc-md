---
title: 将所有工作表列放在单个页面上 PDF
type: docs
weight: 70
url: /zh/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

有时您想要生成一个 PDF 文件，以将工作表的所有列放入一个页面。这[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)属性以非常易于使用的方式提供此功能。输出 PDF 页面的高度和宽度等复杂计算在内部处理，并基于工作表中的数据。

{{% /alert %}}

## **在单个页面上调整工作表列 PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)确保将工作表的所有列呈现到单个 PDF 页面，尽管行可能会扩展到多个页面，具体取决于工作表中的数据。

{{% alert color="primary" %}}

当给定的工作表有很多列时，呈现的 PDF 文件可能会以非常小的尺寸显示内容。在 Acrobat Reader 等查看应用程序中放大时，它仍然可读。

{{% /alert %}}

下面的示例代码显示了如何使用[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)属性呈现 100 列的大型工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好调用[**工作簿.计算公式**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) 方法在将电子表格呈现为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

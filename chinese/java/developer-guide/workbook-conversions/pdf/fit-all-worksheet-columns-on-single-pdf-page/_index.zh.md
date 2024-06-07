---
title: 将所有工作表列适配到单个PDF页面
type: docs
weight: 70
url: /zh/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

有时您希望生成一个 PDF 文件，可以将工作表的所有列放入单个页面中。 [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) 属性以一种非常易于使用的方式提供了此功能。输出 PDF 页面的高度和宽度等复杂计算由内部处理，并根据工作表中的数据进行调整。

{{% /alert %}}

## **将工作表列适配到单个PDF页面**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) 确保将工作表的所有列呈现为单个 PDF 页面，尽管根据工作表中的数据，行可能会扩展为多个页面。

{{% alert color="primary" %}}

当给定工作表具有许多列时，呈现的 PDF 文件内容可能很小。在查看应用程序（如 Acrobat Reader）中放大时仍然可读。

{{% /alert %}}

下面的示例代码展示了如何使用 [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) 属性呈现包含 100 列的大型工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为 PDF 格式之前调用 [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula() 方法。这样做将确保重新计算公式依赖值，并在 PDF 中呈现正确的值。

{{% /alert %}}

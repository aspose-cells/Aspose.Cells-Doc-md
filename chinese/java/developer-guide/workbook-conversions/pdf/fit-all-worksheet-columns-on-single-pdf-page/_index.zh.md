---
title: 将所有工作表列调整到单个PDF页面
type: docs
weight: 70
url: /zh/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

有时，您希望生成一个将工作表的所有列都放入单个页面的PDF文件。[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)属性以一种非常易于使用的方式提供了此功能。输出PDF页面的高度和宽度等复杂计算在内部处理，这些计算是基于工作表中的数据的。

{{% /alert %}}

## **使工作表列适合单个PDF页面**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)可以确保将工作表的所有列呈现为单个PDF页面，尽管行可能因工作表中的数据而扩展到几个页面。

{{% alert color="primary" %}}

当给定的工作表有许多列时，呈现的PDF文件可能会以非常小的尺寸显示内容。当在观看应用程序（例如Acrobat Reader）中放大时仍然可读。

{{% /alert %}}

下面的示例代码显示了如何使用[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)属性来呈现包含100列的大工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格渲染为 PDF 格式之前调用 [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) 方法。这样做将确保重新计算公式依赖的值，并在 PDF 中呈现正确的值。

{{% /alert %}}

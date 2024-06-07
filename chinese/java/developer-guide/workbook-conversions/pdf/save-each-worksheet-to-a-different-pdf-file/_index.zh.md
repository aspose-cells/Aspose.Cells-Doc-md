---
title: 将每个工作表保存为单独的 PDF 文件
type: docs
weight: 50
url: /zh/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells 支持将包含图像、图表等的电子表格文件转换为 PDF 文档。Aspose.Cells for Java 可以独立工作，将电子表格转换为 PDF 文档，无需再使用 Aspose.PDF for Java 进行转换。该转换也不需要创建/使用任何临时文件，整个过程可以在内存中完成。

{{% /alert %}}

如果您需要将模板 Excel 文件中的每个工作表保存为不同的 PDF 文件，这可以很容易地实现。您可以尝试一次为 **[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** 选项设置一个工作表索引以渲染为 PDF。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将电子表格呈现为 PDF 之前调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula() 方法。这样可以确保公式依赖的值重新计算，并在 PDF 中呈现正确的值。

{{% /alert %}}

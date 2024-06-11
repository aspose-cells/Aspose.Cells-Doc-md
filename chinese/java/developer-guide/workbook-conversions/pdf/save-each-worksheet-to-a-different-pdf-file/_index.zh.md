---
title: 将每个工作表保存为不同的PDF文件
type: docs
weight: 50
url: /zh/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells支持将包含图像、图表等的电子表格文件转换为PDF文档。 Aspose.Cells for Java 可独立工作以将电子表格转换为PDF文档，您不需要再使用Aspose.PDF for Java进行转换，转换不需要创建/使用任何临时文件，因为整个过程可以在内存中完成。

{{% /alert %}}

如果您需要将模板Excel文件中的每个工作表保存为生成不同的PDF文件，这可以很容易实现。您可以尝试一次为**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**选项设置一个工作表索引以渲染为PDF。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()）方法。这样可以确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

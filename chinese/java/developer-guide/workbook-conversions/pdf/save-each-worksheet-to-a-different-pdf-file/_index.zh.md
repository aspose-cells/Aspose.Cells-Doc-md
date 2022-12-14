---
title: 将每个工作表保存到不同的 PDF 文件
type: docs
weight: 50
url: /zh/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells 支持将电子表格文件（包含图像、图表等）转换为 PDF 文档。 Aspose.Cells for Java 可以独立工作将电子表格转换为PDF文档，您不再需要使用Aspose.PDF for Java 进行转换。转换也不需要创建/使用任何临时文件，因为整个过程可以在内存中完成。

{{% /alert %}}

如果您需要将每个工作表保存在您的模板 Excel 文件中以生成不同的 PDF 文件。这很容易实现。您可以尝试隐藏文件中的工作表，并根据渲染 PDF 的方式一次显示一张工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[**工作簿.计算公式**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()方法就在将电子表格呈现为 PDF 之前。这可确保重新计算依赖于公式的值，并在 PDF 中呈现正确的值。

{{% /alert %}}

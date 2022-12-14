---
title: 使所有工作表列都适合单个 PDF 页面
type: docs
weight: 160
url: /zh/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

有时您想要生成一个 PDF 文件，使工作表的所有列都适合一页。这[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)属性以非常易于使用的方式提供此功能。输出 PDF 的高度和宽度等复杂计算在内部处理，并基于工作表中的数据。

{{% /alert %}}

## **在单个 PDF 页面上调整工作表列**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)确保工作表中的所有列都呈现为单个 PDF 页面，尽管根据工作表中的数据，行可能会扩展到多个页面。

下面的示例代码展示了如何使用[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)属性呈现 100 列的大型工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

当给定的工作表有很多列时，呈现的 PDF 文件可能会以非常小的尺寸显示内容。在 Acrobat Reader 等查看应用程序中放大时，它仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好调用[**工作簿.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)就在将电子表格呈现为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

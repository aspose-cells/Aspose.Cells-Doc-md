---
title: 将所有工作表列调整到单个PDF页面
type: docs
weight: 160
url: /zh/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

有时候，您希望生成一个PDF文件，将工作表的所有列适合一页。[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)属性以一种非常易于使用的方式提供了这种功能。输出PDF的高度和宽度等复杂计算是在内部处理的，是基于工作表中的数据。

{{% /alert %}}

## **使工作表列适合单个PDF页面**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)确保工作表中的所有列都呈现在单个PDF页面上，尽管根据工作表中的数据，行可能会扩展到几页。

下面的示例代码显示了如何使用[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)属性呈现一个包含100列的大型工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

当给定的工作表有很多列时，渲染的PDF文件可能以非常小的尺寸显示内容。在类似Acrobat Reader的查看应用程序中缩放后仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

---
title: 将所有工作表列适配到单个PDF页面
type: docs
weight: 160
url: /zh/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

有时您想生成一个将工作表的所有列适配到一个页面上的PDF文件。[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)属性以一种非常易于使用的方式提供了这个功能。输出PDF的高度和宽度等复杂计算由内部处理，基于工作表中的数据。

{{% /alert %}}

## **将工作表列适配到单个PDF页面**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)确保工作表中的所有列都呈现在单个PDF页面上，尽管根据工作表中的数据，行可能会扩展到几个页面。

下面的示例代码展示了如何使用[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)属性呈现具有100列的大型工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

当给定的工作表有很多列时，呈现的PDF文件可能以非常小的尺寸显示内容。当在查看应用程序中放大时，它仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算公式相关值，并且正确的值呈现在PDF中。

{{% /alert %}}

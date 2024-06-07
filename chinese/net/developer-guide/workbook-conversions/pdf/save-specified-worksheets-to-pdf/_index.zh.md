---
title: 将指定的工作表保存为 PDF
type: docs
weight: 140
url: /zh/net/save-specified-worksheets-to-pdf/
---

默认情况下，Aspose.Cells 将工作簿中所有**可见**的工作表保存到 pdf 文件中。通过使用 **[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** 选项，您可以将指定的工作表保存到 pdf 文件中。例如，您可以保存活动工作表为 pdf，将所有工作表（可见的和隐藏的工作表）保存为 pdf，将自定义多个工作表保存为 pdf。

## **将活动工作表保存为PDF**

如果你只想要将活动工作表导出为PDF，你可以通过将 **[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)** 传递给 **[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** 选项来实现。

工作表 `Sheet2` 是源文件 [sheetset-example.xlsx](sheetset-example.xlsx) 的活动工作表。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **将所有工作表保存为PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)** 表示工作簿中可见的工作表，**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** 表示工作簿中的所有工作表，包括可见和隐藏/不可见的工作表。如果你想要导出所有工作表到PDF，你只需将 **[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells/rendering/sheetset/all/)** 传递给 **[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** 选项。

源文件 [sheetset-example.xlsx](sheetset-example.xlsx) 包含所有四个工作表，其中隐藏工作表为 `Sheet3`。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **保存指定的工作表至PDF**
如果你想要将所需/自定义的多个工作表导出为PDF，你可以通过将多个工作表索引传递给 **[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** 选项来实现。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

如果你的电子表格包含公式，最好在将电子表格渲染为PDF格式之前调用 [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做可以确保重新计算基于公式的值，并且以正确的值呈现在PDF中。

{{% /alert %}}

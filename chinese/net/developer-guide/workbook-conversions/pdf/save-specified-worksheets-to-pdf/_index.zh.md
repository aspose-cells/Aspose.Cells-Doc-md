---
title: 将指定的工作表保存到 PDF
type: docs
weight: 140
url: /zh/net/save-specified-worksheets-to-pdf/
---
默认情况下，Aspose.Cells 保存所有**可见的**将工作簿中的工作表转换为 pdf 文件。和**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**选项，您可以将指定的工作表保存为 pdf 文件。例如，您可以将活动工作表保存为 pdf、将所有工作表（可见和隐藏工作表）保存为 pdf、将自定义多个工作表保存为 pdf。

##  **将活动工作表保存到 PDF**

如果您只想将活动工作表导出为 pdf，您可以通过传递**[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)**到**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**选项。

 sheet `Sheet2`是源文件的active sheet[图纸集示例.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

##  **将所有工作表保存到 PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)**表示工作簿中的可见工作表，并且**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)**表示工作簿中的所有工作表，包括可见工作表和隐藏/不可见工作表。如果你想将所有工作表导出为pdf，你可以通过**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)**到**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**选项。

源文件[图纸集示例.xlsx](sheetset-example.xlsx)包含所有四张纸和隐藏纸 `Sheet3`。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

##  **将指定的工作表保存到 PDF**
如果您想将所需/自定义的多张工作表导出为 pdf，您可以通过将多张工作表索引传递给**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**选项。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为 PDF 格式之前调用 [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

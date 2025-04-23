---
title: 将指定的工作表保存为 PDF
type: docs
weight: 140
url: /zh/net/save-specified-worksheets-to-pdf/
---

默认情况下，Aspose.Cells 将所有 **可见** 的工作表保存到 PDF 文件中。使用 [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) 选项，您可以将指定的工作表保存到 PDF 文件中。例如，您可以保存活动工作表到 PDF，保存所有工作表（包括可见和隐藏的工作表）到 PDF，将自定义多个工作表保存到 PDF。

## **将活动工作表保存为 PDF**

如果您只想将活动工作表导出为 PDF，则可以通过将 [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) 传递给 [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) 选项来实现。

工作表 `Sheet2` 是源文件[sheetset-example.xlsx](sheetset-example.xlsx)的活动工作表。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **将所有工作表保存为 PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) 指示工作簿中的可见工作表，[**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) 指示工作簿中包括可见工作表和隐藏/不可见工作表。如果您想将所有工作表导出为 PDF，只需将 [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) 传递给 [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) 选项。

源文件[sheetset-example.xlsx](sheetset-example.xlsx)包含所有四个工作表，其中隐藏了工作表`Sheet3`。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **将指定的工作表保存为 PDF**
如果要将所需/自定义的多个工作表导出为 PDF，可以通过将多个工作表索引传递给 [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) 选项来实现。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## ** 将工作表重新排序为 PDF**

如果您希望在不修改源文件的情况下，将工作表以不同顺序（如逆序）导出为PDF，可以通过传递重新排序的工作表索引到 [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) 选项实现。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

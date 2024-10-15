---
title: Save Specified Worksheets to PDF
type: docs
weight: 140
url: /net/save-specified-worksheets-to-pdf/
---

By default, Aspose.Cells save all **visible** worksheets in a workbook to pdf file. With [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) option, you can save specified worksheets to pdf file. e.g. you can save active worksheet to pdf, save all worksheets(both visible and hidden worksheets) to pdf, save custom multiple worksheets to pdf.

## **Save Active Worksheet to PDF**

If you want to only export active sheet to pdf, you can achieve this by passing [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) to [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) option.

The sheet `Sheet2` is the acitve sheet of the source file [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Save  All Worksheets to PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) indicates visible sheets in a workbook, and [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) indicates all sheets including both visible sheets and hidden/invisible sheets in a workbook. If you want to export all sheets to pdf, you can just pass  [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) to [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) option.

The source file [sheetset-example.xlsx](sheetset-example.xlsx) contains all four sheets with hidden sheet `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Save Specified Worksheets to PDF**
If you want to export desired/custom multiple sheets to pdf, you can achieve this by passing multiple sheet indices to [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) option.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **Reorder Worksheets to PDF**

If you want to reorder sheets(e.g. in reverse order) to pdf without modify the source file, you can achieve this by passing reodered sheet indices to [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) option.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
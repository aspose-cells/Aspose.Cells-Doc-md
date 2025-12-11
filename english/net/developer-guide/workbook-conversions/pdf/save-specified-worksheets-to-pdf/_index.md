---
title: Save Specified Worksheets to PDF
type: docs
weight: 140
url: /net/save-specified-worksheets-to-pdf/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

By default, Aspose.Cells **saves** all **visible** worksheets in a workbook to a **PDF** file. With the **[PdfSaveOptions.SheetSet](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option, you can save specified worksheets to a PDF file, e.g., you can save the active worksheet to PDF, save all worksheets (both visible and hidden) to PDF, or save custom multiple worksheets to PDF.

## **Save Active Worksheet to PDF**

If you want to export only the active sheet to PDF, you can achieve this by passing **[SheetSet.Active](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)** to **[PdfSaveOptions.SheetSet](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option.

The sheet `Sheet2` is the **active** sheet of the source file [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Save All Worksheets to PDF**

**[SheetSet.Visible](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)** indicates visible sheets in a workbook, and **[SheetSet.All](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** indicates all sheets, including both visible sheets and hidden/invisible sheets in a workbook. If you want to export all sheets to PDF, you can simply pass **[SheetSet.All](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** to **[PdfSaveOptions.SheetSet](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option.

The source file [sheetset-example.xlsx](sheetset-example.xlsx) contains all four sheets with hidden sheet `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Save Specified Worksheets to PDF**

If you want to export desired/custom multiple sheets to PDF, you can achieve this by passing multiple sheet indices to the **[PdfSaveOptions.SheetSet](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **Reorder Worksheets to PDF**

If you want to reorder sheets (e.g., in reverse order) to PDF without modifying the source file, you can achieve this by passing **reordered** sheet indices to the **[PdfSaveOptions.SheetSet](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** option.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call **[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}

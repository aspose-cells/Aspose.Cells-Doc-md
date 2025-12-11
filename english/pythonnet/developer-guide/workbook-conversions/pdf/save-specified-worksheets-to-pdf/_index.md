---
title: Save Specified Worksheets to PDF
type: docs
weight: 140
url: /python-net/save-specified-worksheets-to-pdf/
description: Learn how to Save Specified Worksheets to PDF with Aspose.Cells for Python via .NET API.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

By default, Aspose.Cells for Python via .NET **saves** all **visible** worksheets in a workbook to a **PDF** file. With the **PdfSaveOptions.sheet_set** option, you can save specified worksheets to a PDF file. For example, you can save the active worksheet to PDF, save all worksheets (both visible and hidden) to PDF, or save custom multiple worksheets to PDF.

## **Save Active Worksheet to PDF**

If you only want to export the active sheet to **PDF**, you can achieve this by passing [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) to [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) option.

The sheet `Sheet2` is the **active** sheet of the source file [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Save All Worksheets to PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) indicates visible sheets in a workbook, and [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) indicates all sheets, including both visible sheets and hidden/invisible sheets in a workbook. If you want to export all sheets to **PDF**, you can simply pass [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) to [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) option.

The source file [sheetset-example.xlsx](sheetset-example.xlsx) contains all four sheets with hidden sheet `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Save Specified Worksheets to PDF**

If you want to export desired/custom multiple sheets to **PDF**, you can achieve this by passing multiple sheet indices to [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) option.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}

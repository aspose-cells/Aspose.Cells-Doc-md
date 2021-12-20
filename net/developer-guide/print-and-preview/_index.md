---
title: Print and Preview
type: docs
weight: 185
url: /net/print-and-preview/
aliases: [/net/printing-workbooks/]
---

{{% alert color="primary" %}}

After creating a worksheet, you often want to print a hard copy of it. This article explains how to print spreadsheets with Aspose.Cells.

{{% /alert %}}

## **Introduction**

Microsoft Excel assumes that you want to print the entire worksheet area unless you specify a selection. To print using Aspose.Cells, first import the Aspose.Cells.Rendering namespace to the program. It has several useful classes, for example, [**SheetRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) and [**WorkbookRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Print Using SheetRender**

The [**Aspose.Cells.Rendering.SheetRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class represents a worksheet and has the [**ToPrinter**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) method which can print a worksheet. The following sample code shows how to print a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Print Using WorkbookRender**

To print a whole workbook, iterate through the sheets and print them, or use the [**WorkbookRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) class.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells also provides overloads for the [**WorkbookRender.ToPrinter()**](https://apireference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) and [**SheetRender.ToPrinter()**](https://apireference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) methods, so it's possible to set the print job name while printing Excel spreadsheets. By default, all print jobs are created with the name "Document".

{{% /alert %}}

## **Advance topics**
- [Convert Worksheet to Image - Remove whitespace around data](/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Converting Worksheet to Image and Worksheet to Image by Page](/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Converting Worksheet to Image using ImageOrPrint Options](/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Export Range of Cells in a Worksheet to Image](/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Export Worksheet or Chart into Image with Desired Width and Height](/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extract Images from Worksheets using ImageOrPrintOptions](/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generate Thumbnail of the Worksheet](/net/generate-thumbnail-of-the-worksheet/)
- [Output Blank Page when there is Nothing to Print](/net/output-blank-page-when-there-is-nothing-to-print/)
- [Page Setup and Printing Options](/net/page-setup-and-printing-options/)
- [Printing Range of Pages using SheetRender and WorkbookRender](/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions](/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Render Worksheet to Graphic Context](/net/render-worksheet-to-graphic-context/)
- [Set Default Font while rendering spreadsheet to images](/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Specify Job or Document Name while printing with Aspose.Cells](/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
- [Worksheet to Image - Set Pixel Format for the Rendered Image](/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
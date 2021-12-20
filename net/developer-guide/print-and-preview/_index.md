---
title: Print and Preview
type: docs
weight: 185
url: /net/print-and-preview/
aliases: [/net/printing-workbooks/,/net/workbook-and-worksheet-print-preview/]
---

{{% alert color="primary" %}}

After creating a worksheet, you often want to print a hard copy of it. This article explains how to print spreadsheets with Aspose.Cells.

{{% /alert %}}

## **Print Introduction**

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

## **Print Preview**

There may be cases where Excel files with millions of pages need to be converted to PDF or images. Processing such files will consume a lot of time and resources. In such cases, the Workbook and Worksheet Print Preview feature might prove to be useful. Before converting such files, the user can check the total number of pages and then decide whether the file is to be converted or not. This article focuses on using the [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) and [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classes to find out the total number of pages.

Aspose.Cells provides the print preview feature. For this, the API provides [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) and [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classes. To create the print preview of the whole workbook, create an instance of the [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) class by passing [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) and [**ImageOrPrintOptions**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objects to the constructor. The [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) class provides an [**EvaluatedPageCount**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) method which returns the number of pages in the generated preview. Similar to [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) class, the [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) class is used to generate a print preview for a specific worksheet. To create the print preview of a worksheet, create an instance of the [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) class by passing [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) and [**ImageOrPrintOptions**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objects to the constructor. The [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) class also provides an [**EvaluatedPageCount**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) method which returns the number of pages in the generated preview.

The following code snippet demonstrates the use of both [**WorkbookPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) and [**SheetPrintingPreview**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classes by using the [sample excel file](94896177.xlsx).

### **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

The following is the output generated by executing the above code.

### **Console Output**

Workbook page count: 1
Worksheet page count: 1


## **Advance topics**
- [Convert Worksheet to Image - Remove whitespace around data](/cells/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Converting Worksheet to Image and Worksheet to Image by Page](/cells/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Converting Worksheet to Image using ImageOrPrint Options](/cells/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Export Range of Cells in a Worksheet to Image](/cells/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Export Worksheet or Chart into Image with Desired Width and Height](/cells/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extract Images from Worksheets using ImageOrPrintOptions](/cells/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generate Thumbnail of the Worksheet](/cells/net/generate-thumbnail-of-the-worksheet/)
- [Output Blank Page when there is Nothing to Print](/cells/net/output-blank-page-when-there-is-nothing-to-print/)
- [Page Setup and Printing Options](/cells/net/page-setup-and-printing-options/)
- [Printing Range of Pages using SheetRender and WorkbookRender](/cells/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions](/cells/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Render Worksheet to Graphic Context](/cells/net/render-worksheet-to-graphic-context/)
- [Set Default Font while rendering spreadsheet to images](/cells/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Specify Job or Document Name while printing with Aspose.Cells](/cells/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
- [Worksheet to Image - Set Pixel Format for the Rendered Image](/cells/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
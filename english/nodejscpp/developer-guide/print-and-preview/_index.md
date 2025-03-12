---  
title: Print and Preview workbook with Node.js via C++  
linktitle: Print and Preview  
type: docs  
weight: 70  
url: /nodejs-cpp/workbook-and-worksheet-print-preview/  
description: Aspose.Cells supports printing and previewing Excel files without Microsoft Excel installation using Node.js via C++.  
---  

{{% alert color="primary" %}}  
After creating a worksheet, you often want to print a hard copy of it. This article explains how to print spreadsheets with Aspose.Cells.  
{{% /alert %}}  

## **Print Introduction**  

Microsoft Excel assumes that you want to print the entire worksheet area unless you specify a selection. To print using Aspose.Cells for Node.js, first import the Aspose.Cells.Rendering module to the program. It has several useful classes, for example, [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) and [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/).  

### **Print Using SheetRender**  

The [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) class represents a worksheet and has the [**toPrinter**](https://reference.aspose.com/cells/nodejs-cpp/cells.rendering/sheetrender/methods/toprinter/index) method which can print a worksheet. The following sample code shows how to print a worksheet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Instantiate a workbook with Excel file.
const workbook = new AsposeCells.Workbook(filePath);

let printerName = "";

while (!printerName || !printerName.trim()) {
    console.log("Please Enter Your Printer Name:");
    printerName = require('readline-sync').question();
}

// Define a worksheet.
// Get the second sheet.
const worksheet = workbook.getWorksheets().get(1);

// Apply different Image/Print options.
const options = new AsposeCells.Rendering.ImageOrPrintOptions();
options.setPrintingPage(AsposeCells.Rendering.PrintingPageType.Default);
const sr = new AsposeCells.Rendering.SheetRender(worksheet, options);

console.log("Printing SampleBook.xlsx");
// Print the sheet.
try {
    sr.toPrinter(printerName);
    console.log("Printing finished.");
} catch (ex) {
    console.log(ex.message);
}
```  

### **Print Using WorkbookRender**  

To print a whole workbook, iterate through the sheets and print them, or use the [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/) class.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();

// Instantiate a workbook with an Excel file.
const filePath = path.join(sourceDir, "samplePrintingUsingWorkbookRender.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const printerName = "doPDF 8";

// Apply different Image/Print options.
const options = new AsposeCells.ImageOrPrintOptions();
options.setImageType(AsposeCells.ImageType.Tiff);
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// To print a whole workbook, iterate through the sheets and print them, or use the WorkbookRender class.
const wr = new AsposeCells.WorkbookRender(workbook, options);

try {
    // Print the workbook.
    wr.toPrinter(printerName);
} catch (ex) {
    console.log(ex.message);
}
```  

{{% alert color="primary" %}}  
Aspose.Cells also provides overloads for the [**WorkbookRender.toPrinter()**](https://reference.aspose.com/cells/nodejs-cpp/cells.rendering.workbookrender/toprinter/methods/3) and [**SheetRender.toPrinter()**](https://reference.aspose.com/cells/nodejs-cpp/cells.rendering.sheetrender/toprinter/methods/2) methods, so it's possible to set the print job name while printing Excel spreadsheets. By default, all print jobs are created with the name "Document".  
{{% /alert %}}  

## **Print Preview**  

There may be cases where Excel files with millions of pages need to be converted to PDF or images. Processing such files will consume a lot of time and resources. In such cases, the Workbook and Worksheet Print Preview feature might prove to be useful. Before converting such files, the user can check the total number of pages and then decide whether the file is to be converted or not. This article focuses on using the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) classes to find out the total number of pages.  

Aspose.Cells provides the print preview feature. For this, the API provides [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) classes. To create the print preview of the whole workbook, create an instance of the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) class by passing [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) objects to the constructor. The [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) class provides an [**evaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) method which returns the number of pages in the generated preview. Similar to [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) class, the [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) class is used to generate a print preview for a specific worksheet. To create the print preview of a worksheet, create an instance of the [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) class by passing [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) objects to the constructor. The [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) class also provides an [**evaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) method which returns the number of pages in the generated preview.  

The following code snippet demonstrates the use of both [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) classes by using the [sample excel file](94896177.xlsx).  

### **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.getSourceDirectory();

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

The following is the output generated by executing the above code.  

### **Console Output**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Advance topics**  
- [Configuring Fonts for Rendering Spreadsheets](/cells/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convert Worksheet to Image - Remove whitespace around data](/cells/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Converting Worksheet to Image and Worksheet to Image by Page](/cells/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Converting Worksheet to Image using ImageOrPrint Options](/cells/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Export Range of Cells in a Worksheet to Image](/cells/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Export Worksheet or Chart into Image with Desired Width and Height](/cells/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extract Images from Worksheets using ImageOrPrintOptions](/cells/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generate Thumbnail of the Worksheet](/cells/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Output Blank Page when there is Nothing to Print](/cells/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Page Setup and Printing Options](/cells/nodejs-cpp/page-setup-and-printing-options/)  
- [Printing Range of Pages using SheetRender and WorkbookRender](/cells/nodejs-cpp/printing-range-of-pages-using-sheetrender-and-workbookrender/)  
- [Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions](/cells/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Render Worksheet to Graphic Context](/cells/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Specify Individual or Private Set of Fonts for Workbook Rendering](/cells/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)  
- [Specify Job or Document Name while printing with Aspose.Cells](/cells/nodejs-cpp/specify-job-or-document-name-while-printing-with-aspose-cells/)  
  
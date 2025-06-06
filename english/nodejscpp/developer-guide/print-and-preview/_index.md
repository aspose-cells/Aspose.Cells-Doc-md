---  
title: Preview workbook with Node.js via C++  
linktitle: Preview workbook 
type: docs  
weight: 70  
url: /nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells supports printing and previewing Excel files without Microsoft Excel installation using Node.js via C++.  
---  

## **Print Preview**  

There may be cases where Excel files with millions of pages need to be converted to PDF or images. Processing such files will consume a lot of time and resources. In such cases, the Workbook and Worksheet Print Preview feature might prove to be useful. Before converting such files, the user can check the total number of pages and then decide whether the file is to be converted or not. This article focuses on using the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) classes to find out the total number of pages.  

Aspose.Cells provides the print preview feature. For this, the API provides [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) classes. To create the print preview of the whole workbook, create an instance of the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) class by passing [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) objects to the constructor. The [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) class provides an [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) method which returns the number of pages in the generated preview. Similar to [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) class, the [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) class is used to generate a print preview for a specific worksheet. To create the print preview of a worksheet, create an instance of the [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) class by passing [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) objects to the constructor. The [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) class also provides an [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) method which returns the number of pages in the generated preview.  

The following code snippet demonstrates the use of both [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) classes by using the [sample excel file](94896177.xlsx).  

### **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

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
- [Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions](/cells/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Render Worksheet to Graphic Context](/cells/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Specify Individual or Private Set of Fonts for Workbook Rendering](/cells/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   
  
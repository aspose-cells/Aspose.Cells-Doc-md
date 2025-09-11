---
title: Pdf with Node.js via C++
linktitle: Pdf
type: docs
weight: 220
url: /nodejs-cpp/convert-excel-to-pdf/
description: Learn how to convert Excel Workbook into PDF using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells supports conversion of Excel Workbook into PDF. In this example, we will see the complete conversion of an Excel Workbook into PDF.
{{% /alert %}}

## **Converting Excel Workbook to PDF**

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for Node.js via C++ populates **PDF Producer** field with value, e.g 'Aspose.Cells v23.2'.

Please note that you can change this information in output Documents by [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--) property.
{{% /alert %}}

### **Direct Conversion**

Aspose.Cells for Node.js via C++ supports conversion from spreadsheets to PDF independently of other software. Simply save an Excel file to PDF using the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) method. The [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) method provides the [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration member that converts the native Excel files to PDF format.

Follow the below steps to directly convert the Excel spreadsheets to PDF format:

1. Instantiate an object of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class by calling its empty constructor.
1. You may open/load an existing template file or skip this step if you are creating the workbook from scratch.
1. Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells' APIs.
1. When the spreadsheet code is complete, call the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) method to save the spreadsheet.

The file format should be PDF so select *Pdf* (a pre-defined value) from the [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration to generate the final PDF document.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **Advanced Conversion**

You may also opt to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class gives you control over the print, font, security and compression settings for the output PDF. 

The most important property is [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) which enables you to set the PDF standards compliance level. Currently, you can save to PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, and PDF/A-3u formats. Note that with the PDF/A format, an output file size is larger than a regular PDF file size.

#### **Saving Workbook to PDF/A Complied Files**

The below-provided code snippet demonstrates how to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class to save Excel files to PDF/A compliant PDF format.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
Please note, the [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) property was added with the release of Aspose.Cells for Node.js via C++ 5.3.0.
{{% /alert %}}

#### **Set the PDF Creation Time**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class, you can get or set the PDF creation time. The following code demonstrates the use of [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) property to set the creation time of the PDF file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **Set ContentCopyForAccessibility option**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class, you can get or set the PDF [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) option to control the content access in the converted PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **Export Custom properties to PDF**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class, you can export the custom properties in the source workbook to the PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/) enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on File and then properties option as shown in the following image. Template file "sourceWithCustProps.xlsx"  can be downloaded [here](sourceWithCustProps.xlsx) for testing and output PDF file "outSourceWithCustProps" is available [here](outSourceWithCustProps.pdf) for analysis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **Conversion Attributes**

We work to enhance the conversion features with each new release. Aspose.Cell's Excel to PDF conversion still has a couple of limitations. MapChart is not supported when converting to PDF format. Also, some drawing objects are not supported well.

The table that follows lists all features that are fully or partially supported when exporting to PDF using Aspose.Cells. This table is not final and does not cover all the spreadsheet attributes but it does identify those features that are not supported or partially supported for conversion to PDF.

|**Document Element**|**Attribute**|**Supported**|**Notes**|
| :- | :- | :- | :- |
|Alignment| |Yes| |
|Background settings| |Yes| |
|Border|Color|Yes| |
|Border|Line style|Yes| |
|Border|Line width|Yes| |
|Cell Data| |Yes| |
|Comments| |Yes| |
|Conditional Formatting| |Yes| |
|Document Properties| |Yes| |
|Drawing Objects| |Partially|Shadow and 3-D effects for drawing objects are not supported well; WordArt and SmartArt are partially supported.|
|Font|Size|Yes| |
|Font|Color|Yes| |
|Font|Style|Yes| |
|Font|Underline|Yes| |
|Font|Effects|Yes||
|Images| |Yes| |
|Hyperlink| |Yes| |
|Charts| |Partially|MapChart is not supported.|
|Merged Cells| |Yes| |
|Page Break| |Yes| |
|Page Setup|Header/Footer|Yes| |
|Page Setup|Margins|Yes| |
|Page Setup|Page Orientation|Yes| |
|Page Setup|Page Size|Yes| |
|Page Setup|Print Area|Yes| |
|Page Setup|Print Titles|Yes| |
|Page Setup|Scaling|Yes| |
|Row Height/Column Width| |Yes| |
|RTL (Right to Left) Language| |Yes| |

{{% alert color="primary" %}}
If your spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.
{{% /alert %}}

## **Advance topics**
- [Add PDF Bookmarks with Named Destinations](/cells/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Avoid Blank Page in Output PDF when there is Nothing to Print](/cells/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Change the Font on just the specific Unicode characters while saving to PDF](/cells/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Convert XLSX File to PDF Format](/cells/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [Convert Excel file to PDF format compatible with PDFA-1a](/cells/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convert XLS File with Images or Charts to PDF](/cells/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Create PdfBookmarkEntry for Chart Sheet](/cells/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Fit All Worksheet Columns on Single PDF Page](/cells/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class](/cells/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Get Warnings for Font Substitution while Rendering Excel File](/cells/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignore Errors while Rendering Excel to PDF](/cells/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limit the Number of Pages Generated - Excel to PDF Conversion](/cells/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Print Comments while saving to PDF](/cells/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [Render Office Add-Ins while converting Excel to PDF](/cells/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion](/cells/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Render Unicode Supplementary characters in output PDF by Aspose.Cells](/cells/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resampling Added Images - Excel to PDF Conversion](/cells/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Save Each Worksheet to a Different PDF File](/cells/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Save Excel into PDF with Standard or Minimum Size](/cells/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Save Specified Worksheets to PDF](/cells/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [Secure PDF Documents](/cells/nodejs-cpp/secure-pdf-documents/)
- [Specify how to cross string in output PDF and image](/cells/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
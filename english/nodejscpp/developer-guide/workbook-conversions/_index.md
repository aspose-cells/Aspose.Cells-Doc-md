---  
title: Convert Excel to Pdf, Image and other formats  
linktitle: Workbook Conversions  
type: docs  
weight: 65  
url: /nodejs-cpp/convert-workbook-to-different-formats/  
description: Convert Excel files to Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML and more using Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Aspose.Cells supports conversion between many formats. Technically, conversion means to load a workbook in one file format and save it into another.  
{{% /alert %}}  

## **Convert Excel Workbook to PDF**  
PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.  

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **Convert Excel Workbook to JPG**  
Aspose.Cells supports converting Excel files to JPG. The code example below shows how to save a workbook as JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Convert Excel Workbook to Image**  
Aspose.Cells supports converting Excel files to images. The code example below shows how to save a workbook as images.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **Converting Excel Workbook to XPS**  
The XPS document format consists of structured XML markup that defines the layout of a document and the visual appearance of each page, along with rendering rules for distributing, archiving, rendering, processing, and printing documents.  

The markup language for XPS is a subset of XAML which allows it to incorporate vector graphics elements in documents, using XAML to mark up the Windows Presentation Foundation (WPF) primitives. The elements used are described in terms of paths and other geometrical primitives.  

An XPS file is, in fact, a unicode ZIP archive using the Open Packaging Conventions, containing the files which make up the document. These include an XML markup file for each page, text, embedded fonts, raster images, 2D vector graphics, as well as the digital rights management information. The contents of an XPS file can be examined simply by opening it in an application that supports ZIP files.  

From Aspose.Cells 6.0.0, Microsoft Excel to XPS conversion is supported.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **Convert Excel to Ods, Sxc and Fods (OpenOffice / LibreOffice Calc)**  
Aspose.Cells supports converting Excel files to Ods, Sxc and Fods files. The code example below shows how to convert the [template](book1.xlsx) to Ods, Sxc and Fods file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **Converting Excel Workbook to MHTML Files**  
MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio, and so on) into one file. They are used for emails with the .mht file extension.  

Aspose.Cells supports reading and writing MHTML files.  

The code example below shows how to save a workbook as an MHTML file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **Converting Excel Workbook to HTML**  
The Aspose.Cells API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells uses the [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) class to provide the flexibility to control several aspects of the output HTML.  

The code example below shows how to save a workbook as an HTML file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **Setting the Image Preferences for HTML**  
Starting from 8.0.2, Aspose.Cells has exposed [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) for the [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) class, allowing developers to specify image preferences when saving spreadsheets to HTML format.  

Below are details of some of the image settings that can be applied,  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): Specifies the image type. Please note, all shapes, including charts, render as images in the output HTML.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): Specifies the quality of the image between 0 to 100, when [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) is specified as Jpeg.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): Gets or sets the vertical resolution of the image in dots per inch.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): Gets or sets the horizontal resolution of the image in dots per inch.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): Gets or sets the compression type for the images when [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) is specified as Tiff.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): Indicates if the background of an image should be transparent when ImageFormat is specified as Png.  

## **Convert Excel Workbook to Markdown**  
The Aspose.Cells API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) as the second parameter of [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) method. You may also use [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) class to specify additional settings for exporting worksheet to Markdown.  

The following code example demonstrates exporting active worksheet to Markdown by using [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration member. Please see the [output Markdown file](md_sample.txt) generated by the code for reference.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **Convert Excel Workbook to JSON**  
Aspose.Cells supports converting a workbook to Json (JavaScript Object Notation) file.  

The following code example demonstrates exporting active worksheet to Json by using [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration member. Please see the code to convert [source file](Book1.xlsx) to the [output Json file](Book1.Json) generated by the code for reference.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Convert Excel to XML**  
Aspose.Cells supports converting a workbook to Excel 2003 Spreadsheet XML and plain XML data.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **Convert Excel Workbook to TIFF**  
Aspose.Cells supports converting a workbook to TIFF file.  

The code snippet below shows how to convert Excel to TIFF:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **Convert Excel Workbook to DOCX**  
The Aspose.Cells API provides support for converting spreadsheets to DOCX format. To export the workbook to DOCX, pass [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) as the second parameter of [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) method. You may also use [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) class to specify additional settings for exporting worksheet to DOCX.  

The following code example demonstrates exporting active worksheet to DOCX by using [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration member. Please see the [output DOCX file](Book1.docx) generated by the code for reference.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **Convert Excel Workbook to PPTX**  
The Aspose.Cells API provides support for converting spreadsheets to PPTX format. To export the workbook to PPTX, pass [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) as the second parameter of [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) method. You may also use [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) class to specify additional settings for exporting worksheet to PPTX.  

The following code example demonstrates exporting active worksheet to PPTX by using [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration member. Please see the [output PPTX file](Book1.pptx) generated by the code for reference.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **Convert Excel Workbook to EPUB**  
The Aspose.Cells API provides support for converting spreadsheets to EPUB format. To export the workbook to EPUB, pass [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) as the second parameter of [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) method. You may also use [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) class to specify additional settings for exporting worksheet to Epub.  

The following code example demonstrates exporting active worksheet to EPUB by using [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration member.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **Convert Excel Workbook to AZW3**  
The Aspose.Cells API provides support for converting spreadsheets to AZW3 format. To export the workbook to AZW3, pass [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) as the second parameter of [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) method. You may also use [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) class to specify additional settings for exporting worksheet to AZW3.  

The following code example demonstrates exporting active worksheet to AZW3 by using [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration member.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **Advance topics**  
- [Convert Revision of XLSB to XLSM](/cells/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/nodejs-cpp/convert-excel-to-html/)  
- [Image](/cells/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/nodejs-cpp/convert-workbook-to-json/)  
- [Convert Excel workbook to Ods, Sxc and Fods (OpenOffice / LibreOffice calc).](/cells/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Convert Excel to CSV, TSV and Txt](/cells/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Track Document Conversion Progress](/cells/nodejs-cpp/track-document-conversion-progress/)  
- [Convert CSV, TSV and TXT to Excel](/cells/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  
  
{{< app/cells/assistant language="nodejs-cpp" >}}

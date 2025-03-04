---
title: Different Ways to Save Files with Node.js via C++
linktitle: Save Files
type: docs
weight: 40
url: /nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++ can save files to different formats including PDF, HTML, DOCX, PPTX, JSON, and MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and more using Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to create and save files. This article explains the various ways in which files can be saved.

{{% /alert %}}

## **Different Ways to Save Files**

Aspose.Cells provides the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) which represents a Microsoft Excel file and provides the properties and methods necessary to work with Excel files. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class provides the [**save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat) method used to save Excel files. The [**save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat) method has many overloads that are used to save files in different ways.

The file format that the file is saved to is decided by the [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration

|**File Format Types**|**Description**|
| :- | :- |
|CSV|Represents a CSV file|
|Excel97To2003|Represents an Excel 97 - 2003 file|
|Xlsx|Represents an Excel 2007 XLSX file|
|Xlsm|Represents an Excel 2007 XLSM file|
|Xltx|Represents an Excel 2007 template XLTX file|
|Xltm|Represents an Excel 2007 macro-enabled XLTM file|
|Xlsb|Represents an Excel 2007 binary XLSB file|
|SpreadsheetML|Represents a Spreadsheet XML file|
|TSV|Represents a Tab-separated values file|
|TabDelimited|Represents a Tab Delimited text file|
|ODS|Represents an ODS file|
|Html|Represents HTML file(s)|
|MHtml|Represents an MHTML file(s)|
|Pdf|Represents a PDF file|
|XPS|Represents an XPS document|
|TIFF|Represents Tagged Image File Format (TIFF)|

## **How to Save File to Different Formats**

To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration) when calling the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) object's [**save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat) method.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **How to Save Workbook to Pdf**
Portable Document Format (PDF) is a type of document created by Adobe back in the 1990s. The purpose of this file format was to introduce a standard for representation of documents and other reference material in a format that is independent of application software, hardware, as well as Operating System. The PDF file format has full capability to contain information like text, images, hyperlinks, form-fields, rich media, digital signatures, attachments, metadata, Geospatial features, and 3D objects in it that can become part of source document.

The following code shows how to save workbook as pdf file with Aspose.Cells:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **How to Save Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS, and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#separator) is comma, so do not specify a separator if saving to CSV format. Please note: If you are using the evaluation version and even if the [**TxtSaveOptions.exportAllSheets**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#exportAllSheets) property is set to true, the program will still only export one worksheet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **How to Save File to Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```

## **How to Save File to a Stream**

To save files to a stream, create a *MemoryStream* or *FileStream* object and save the file to that stream object by calling the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) object's [**save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat) method. Specify the desired file format using the [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumeration when calling the [**save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat) method.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **How to Save Excel File to Html and Mht files**
Aspose.Cells can simply save an Excel file, JSON, CSV, or other files which could be loaded by Aspose.Cells as .html and .mht files.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```
 

## **How to Save Excel File to OpenOffice (ODS, SXC, FODS, OTS)**
We can save the files as OpenOffice format: ODS, SXC, FODS, OTS, etc.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **How to Save Excel File to JSON or XML**

JSON (JavaScript Object Notation) is an open standard file format for sharing data that uses human-readable text to store and transmit data. JSON files are stored with the .json extension. JSON requires less formatting and is a good alternative for XML. JSON is derived from JavaScript but is a language-independent data format. The generation and parsing of JSON is supported by many modern programming languages. application/json is the media type used for JSON.

Aspose.Cells supports saving files to JSON or XML.

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


## **Advance topics**
- [Adjust workbook compression level](/cells/nodejs-cpp/adjust-workbook-compression-level/)
- [Save Workbook to Strict Open XML Spreadsheet Format](/cells/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Saving File to Response Object](/cells/nodejs-cpp/saving-file-to-response-object/)

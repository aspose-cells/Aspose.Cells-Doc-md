---  
title: Convert Excel file to PDF format compatible with PDF/A-1a with Node.js via C++  
linktitle: Convert Excel file to PDF format compatible with PDF/A-1a  
type: docs  
weight: 130  
url: /nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Learn how to convert Excel files to PDF/A compliant PDF files using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

PDF/A is a unique flavor of PDF designed for the long-term preservation of documents. PDF/A is an ISO-standardized version of the Portable Document Format (PDF) which is an archival format of PDF that embeds all fonts used in the document within the PDF file. PDF/A differs from PDF by prohibiting features, such as font linking (as opposed to font embedding) and encryption. Aspose.Cells for Node.js via C++ enables you to save the Excel files to PDF/A compliant PDF files (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, and PDF/A-3u are supported). This topic describes how to save the Excel workbook to PDF/A compliant (PDF/A-1a) PDF file.  

## **Convert Excel file to PDF Format Compatible with PDF/A-1a**  

Developers may use the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) class gives you control over the print, font, security and compression settings for the output PDF. The most important property is [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) that enables you to save the Excel files to PDF/A compliant PDF files.  

The following sample code explains how to convert an Excel file to PDF format compatible with PDF/A-1a. Please see its [output PDF](outputCompliancePdfA1a.pdf) as well as the screenshot for reference.  

## **Screenshot**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}

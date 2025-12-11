---  
title: Saving File to Response Object with Node.js via C++  
linktitle: Saving File to Response Object  
type: docs  
weight: 50  
url: /nodejs-cpp/saving-file-to-response-object/  
description: Learn how to dynamically generate files and send them directly to a client browser using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Aspose.Cells makes it possible to manipulate files. This article explains the various ways in which files can be saved to a response object.  

{{% /alert %}}  

## **Saving File to Response Object**  

It is also possible to generate a file dynamically and send it directly to a client browser. In order to do so, use a special overloaded version of the [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) method that accepts the following parameters:  

- Node.js response object.  
- File name.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/), the content‑disposition type of the output file.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/), the file format type.  

The [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) enumeration determines whether the file being sent to the browser provides the option to open itself directly in the browser or in an application associated with *.xls*, *.xlsx*, or another extension.  

The enumeration contains the following pre‑defined save types:  

| **Type** | **Description** |  
| :- | :- |  
| Attachment | Sends the spreadsheet to the browser and opens in an application as an attachment associated with *.xls*, *.xlsx* or other extensions |  
| Inline | Sends the document to the browser and presents an option to save the spreadsheet to disk or open inside the browser |  

### **XLS Files**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const workbook = new AsposeCells.Workbook();

// If response is not null
let response = null;

if (response != null) {
    // Save in Excel2003 XLS format
    workbook.save(response, path.join(dataDir, "output.xls"), AsposeCells.ContentDisposition.Inline, new AsposeCells.XlsSaveOptions());
    response.end();
}
```  

### **XLSX Files**  

```javascript
try 
{
    const path = require("path");
    const AsposeCells = require("aspose.cells.node");

    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");
    // Load your source workbook
    const workbook = new AsposeCells.Workbook();

    if (Response != null) {
        // Save in Xlsx format
        workbook.saveAsync(Response, path.join(dataDir, "output.xlsx"), AsposeCells.ContentDisposition.Attachment, new AsposeCells.OoxmlSaveOptions()).then(() => {
            Response.end();
        });
    }
}
```  

### **PDF Files**  

```javascript
try {
    const path = require("path");
    const AsposeCells = require("aspose.cells.node");

    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");
    const filePath = path.join(dataDir, "output.pdf");

    // Creating a Workbook object
    const workbook = new AsposeCells.Workbook();

    if (Response != null) {
        // Save in Pdf format
        workbook.saveAsync(Response, filePath, AsposeCells.ContentDisposition.Attachment, new AsposeCells.PdfSaveOptions()).then(() => {
            Response.end();
        });
    }
}
```  

### **Note**  

Due to the absence of a standard response object in Node.js, this functionality does not exist in Aspose.Cells for Node.js via C++. You can refer to the following code to save the file to the stream, then perform operations on the stream.  

```javascript
const path = require("path");
const { Workbook, SaveFormat } = require("aspose.cells.node");

async function downloadExcel(req, res) {
    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");
    const filePath = path.join(dataDir, "Book1.xlsx");
    // Load your source workbook
    const workbook = new Workbook(filePath);
    // Save the workbook to a memory stream
    const stream = workbook.save(null, SaveFormat.Xlsx);

    // Set the content type and file name
    const contentType = "application/octet-stream";
    const fileName = "output.xlsx";

    // Set the response headers
    res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
    res.setHeader("Content-Type", contentType);

    // Write the file contents to the response body stream
    res.end(stream);

    // Return the response
    return;
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

---  
title: Sparar fil till svar objekt med Node.js via C++  
linktitle: Spara fil till responsobjekt  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/saving-file-to-response-object/  
description: Lär dig hur du dynamiskt genererar filer och skickar dem direkt till en klientwebbläsare med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells gör det möjligt att manipulera filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas till ett responsobjekt.  

{{% /alert %}}  

## **Spara fil till responsobjekt**  

Det är också möjligt att generera en fil dynamiskt och skicka den direkt till en klientwebbläsare. Använd en speciell överbelastad version av [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-)-metoden som accepterar följande parametrar:  

- Node.js svar objekt.  
- Filnamn.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/), utdatafilens content-disposition-typ.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/), filformatstyp  

Enumerationen [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) avgör om filen som skickas till webbläsaren ger möjlighet att öppna den direkt i webbläsaren eller i ett program som är kopplat till .xls/.xlsx eller annan extension.  

Uppräkningen innehåller följande fördefinierade sparalternativ:  

|**Typ**|**Beskrivning**|  
| :- | :- |  
|Bilaga|Skickar kalkylarket till webbläsaren och öppnas i en applikation som en bilaga associerad med .xls/.xlsx eller andra filändelser|  
|Inline|Skickar dokumentet till webbläsaren och presenterar ett alternativ att spara kalkylarket på disken eller öppna det inne i webbläsaren|  

### **XLS-filer**  

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

### **XLSX-filer**  

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
```  

### **PDF-filer**  

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
```  

### **Obs**  

På grund av brist på ett standard svar-objekt i Node.js, finns inte denna funktion i Aspose.Cells for Node.js via C++. Du kan hänvisa till följande kod för att spara filen till strömmen och sedan utföra operationer på strömmen.  

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



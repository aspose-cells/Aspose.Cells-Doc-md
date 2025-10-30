---  
title: Datei an Response Objekt mit Node.js via C++ senden  
linktitle: Datei im Antwortobjekt speichern  
type: docs  
weight: 50  
url: /de/nodejs-cpp/saving-file-to-response-object/  
description: Erfahren Sie, wie Sie Dateien dynamisch generieren und direkt an den Browser des Clients senden, indem Sie Aspose.Cells for Node.js via C++ verwenden.  
---  

{{% alert color="primary" %}}  

Mit Aspose.Cells ist es möglich, Dateien zu manipulieren. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien in einem Antwortobjekt gespeichert werden können.  

{{% /alert %}}  

## **Speichern der Datei im Antwortobjekt**  

Es ist auch möglich, eine Datei dynamisch zu generieren und sie direkt an den Browser des Clients zu senden. Dazu verwenden Sie eine spezielle überladene Version der [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-)-Methode, die die folgenden Parameter akzeptiert:  

- Node.js Antwortobjekt.  
- Dateiname.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/), der Inhalt-Dispositionstyp der Ausgabedatei.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/), der Dateiformat-Typ  

Die Enumeration [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) bestimmt, ob die an den Browser gesendete Datei die Option bietet, sie direkt im Browser oder in einer mit .xls/.xlsx oder einer anderen Erweiterung verbundenen Anwendung zu öffnen.  

Die Enumeration enthält die folgenden vordefinierten Speichertypen:  

|**Typ**|**Beschreibung**|  
| :- | :- |  
|Anhang|Sendet die Tabelle an den Browser und öffnet sie in einer Anwendung als Anhang, der mit .xls/.xlsx oder anderen Erweiterungen verknüpft ist|  
|Inline|Sendet das Dokument an den Browser und bietet die Option, die Tabelle auf der Festplatte zu speichern oder im Browser zu öffnen|  

### **XLS-Dateien**  

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

### **XLSX-Dateien**  

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

### **PDF-Dateien**  

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

### **Hinweis**  

Aufgrund des Fehlens eines Standard-Antwortobjekts in Node.js existiert diese Funktionalität in Aspose.Cells for Node.js via C++ nicht. Sie können den folgenden Code verwenden, um die Datei in den Stream zu speichern und dann Operationen an diesem Stream durchzuführen.  

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

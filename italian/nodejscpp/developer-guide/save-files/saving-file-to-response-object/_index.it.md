---  
title: Salvataggio del file sull oggetto Response con Node.js tramite C++  
linktitle: Salvataggio File in un Oggetto di Risposta  
type: docs  
weight: 50  
url: /it/nodejs-cpp/saving-file-to-response-object/  
description: Impara come generare dinamicamente i file e inviarli direttamente al browser del client usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells rende possibile manipolare i file. Questo articolo spiega i vari modi in cui i file possono essere salvati in un oggetto di risposta.  

{{% /alert %}}  

## **Salvataggio del file nell'oggetto di risposta**  

È anche possibile generare un file dinamicamente e inviarlo direttamente a un browser client. Per farlo, utilizza una versione sovraccaricata speciale del metodo [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) che accetta i seguenti parametri:  

- Oggetto response di Node.js.  
- Nome file.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/), il tipo di content-disposition del file di output.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/), il tipo di formato file.  

L'enumerazione [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) determina se il file inviato al browser offre l'opzione di aprirlo direttamente nel browser stesso o in un'applicazione associata a .xls/.xlsx o altra estensione.  

L'enumerazione contiene i seguenti tipi di salvataggio predefiniti:  

|**Tipo**|**Descrizione**|  
| :- | :- |  
|Allegato|Invia il foglio di calcolo al browser e apre un'applicazione come allegato associato a .xls/.xlsx o altre estensioni|  
|Inline|Invia il documento al browser e presenta un'opzione per salvare il foglio di calcolo sul disco o aprirlo all'interno del browser|  

### **File XLS**  

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

### **File XLSX**  

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

### **File PDF**  

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

### **Nota**  

A causa dell'assenza di un oggetto di risposta standard in Node.js, questa funzionalità non esiste in Aspose.Cells for Node.js via C++. Puoi fare riferimento al seguente codice per salvare il file nello stream, quindi eseguire operazioni sullo stream.  

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

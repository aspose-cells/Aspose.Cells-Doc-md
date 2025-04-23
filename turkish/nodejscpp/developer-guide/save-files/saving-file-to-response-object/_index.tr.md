---  
title: Node.js ile C++ kullanarak Dosyayı Yanıt Nesnesine Kaydetme  
linktitle: Yanıt Nesnesine Dosya Kaydet  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/saving-file-to-response-object/  
description: Aspose.Cells for Node.js via C++ kullanarak dosyaları dinamik olarak nasıl oluşturup doğrudan istemci tarayıcısına göndereceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  

Aspose.Cells, dosyaların manipüle edilmesini mümkün kılar. Bu makale, dosyaların bir yanıt nesnesine nasıl kaydedilebileceğini açıklar.  

{{% /alert %}}  

## **Yanıt Nesnesine Dosya Kaydetme**  

Ayrıca, bir dosyayı dinamik olarak oluşturup doğrudan istemci tarayıcısına göndermek mümkündür. Bunu yapmak için, aşağıdaki parametreleri kabul eden özel aşırı yüklenmiş [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) yöntemi kullanılmalıdır:  

- Node.js yanıt nesnesi.  
- Dosya adı.  
- Çıktı dosyasının içerik düzeni türü olan [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/).  
- Dosya biçim türü olan [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/).  

[**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) enumerasyonu, tarayıcıya gönderilen dosyanın doğrudan tarayıcıda veya .xls/.xlsx ya da başka uzantıya sahip bir uygulamada açma seçeneği sağlayıp sağlamadığını belirler.  

Numaralama aşağıdaki önceden tanımlanmış kaydetme türlerini içerir:  

|**Tür**|**Açıklama**|  
| :- | :- |  
|Ek|Elektronik tabloyu tarayıcıya gönderir ve .xls/.xlsx veya diğer uzantılarla ilişkilendirilmiş bir uygulamada bir eki olarak açar|  
|İçeride|Belgeyi tarayıcıya gönderir ve elektronik tabloyu diske kaydetme veya tarayıcı içinde açma seçeneği sunar|  

### **XLS Dosyaları**  

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

### **XLSX Dosyaları**  

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

### **PDF Dosyaları**  

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

### **Not**  

Node.js'de standart yanıt nesnesinin olmaması nedeniyle, bu özellik Aspose.Cells for Node.js via C++'te mevcut değildir. Dosyayı akışa kaydetmek ve sonra akış üzerinde işlemler yapmak için aşağıdaki kodu kullanabilirsiniz.  

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



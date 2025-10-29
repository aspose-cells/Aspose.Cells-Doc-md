---  
title: Сохранение файла в объект Response с помощью Node.js через C++  
linktitle: Сохранение файла в объект ответа  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/saving-file-to-response-object/  
description: Узнайте, как динамически генерировать файлы и напрямую отправлять их через браузер клиента с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells делает возможным манипулирование файлами. В этой статье объясняются различные способы сохранения файлов в объект ответа.  

{{% /alert %}}  

## **Сохранение файла в объект ответа**  

Также возможно динамически сгенерировать файл и отправить его прямо в браузер клиента. Для этого используйте специальную перегруженную версию метода [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-), которая принимает следующие параметры:  

- Объект ответа Node.js.  
- Имя файла.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/), тип содержания выводимого файла.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/), тип формата файла  

Перечисление [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) определяет, предоставляет ли файл, отправляемый в браузер, возможность открывать его прямо в браузере или через связанное с .xls/.xlsx или другим расширением приложение.  

Перечисление содержит следующие предопределенные типы сохранения:  

|**Тип**|**Описание**|  
| :- | :- |  
|Attachment|Отправляет электронную таблицу в браузер и открывает ее в приложении в качестве вложения, связанного с .xls/.xlsx или другими расширениями|  
|Inline|Отправляет документ в браузер и предоставляет возможность сохранить электронную таблицу на диск или открыть внутри браузера|  

### **XLS Файлы**  

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

### **XLSX Файлы**  

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

### **PDF Файлы**  

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

### **Примечание**  

Из-за отсутствия стандартного объекта ответа в Node.js эта функциональность отсутствует в Aspose.Cells for Node.js via C++. Можно обратиться к следующему коду для сохранения файла в поток, а затем выполнить операции с этим потоком.  

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

---  
title: 通过 C++ 使用 Node.js 将文件保存到响应对象  
linktitle: 将文件保存到响应对象  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/saving-file-to-response-object/  
description: 了解如何使用 Aspose.Cells for Node.js via C++ 动态生成文件并直接将其发送到客户端浏览器。  
---  

{{% alert color="primary" %}}  

Aspose.Cells可以操作文件。本文解释了可以将文件保存到响应对象的各种方法。  

{{% /alert %}}  

## **将文件保存到响应对象**  

也可以动态生成文件并直接发送到客户端浏览器。为此，请使用接受以下参数的 [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) 方法的特殊重载版本：  

- Node.js 响应对象。  
- 文件名。  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/)，输出文件的 content-disposition 类型。  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/)，文件格式类型  

[**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) 枚举决定了传送到浏览器的文件是否提供直接在浏览器或与 .xls/.xlsx 或其他扩展名相关联的应用程序中打开的选项。  

该枚举包含以下预定义的保存类型：  

|**类型**|**描述**|  
| :- | :- |  
|附件|将电子表格发送到浏览器，并作为与.xls/.xlsx或其他扩展名相关联的附件在应用程序中打开|  
|内置|将文档发送到浏览器，并提供选项将电子表格保存到磁盘或在浏览器中打开|  

### **XLS文件**  

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

### **XLSX文件**  

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

### **PDF文件**  

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

### **注意**  

由于 Node.js 中没有标准的响应对象，此功能在 Aspose.Cells for Node.js via C++ 中不存在。您可以参考以下代码将文件保存到流中，然后对流进行操作。  

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



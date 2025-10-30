---  
title: Node.js経由でC++を使用してレスポンスオブジェクトにファイルを保存する方法  
linktitle: レスポンスオブジェクトへのファイルの保存  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/saving-file-to-response-object/  
description: Aspose.Cells for Node.js via C++を使って、ファイルを動的に生成し、クライアントブラウザに直接送信する方法を学びます。  
---  

{{% alert color="primary" %}}  

Aspose.Cellsを使用すると、ファイルを操作することができます。この記事では、ファイルをレスポンスオブジェクトに保存するさまざまな方法を説明します。  

{{% /alert %}}  

## **レスポンスオブジェクトへのファイルの保存**  

また、ファイルを動的に生成してクライアントブラウザに直接送信することも可能です。そのためには、次のパラメータを受け取る特別なオーバーロードされた[**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-)メソッドを使用します。  

- Node.jsのレスポンスオブジェクト。  
- ファイル名。  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/)、出力ファイルのcontent-dispositionタイプ。  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/)、ファイル形式の種類  

[**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/)列挙体は、ブラウザに送信されるファイルがブラウザ内で直接開くオプションを提供するか、.xls/.xlsxまたは他の拡張子に関連付けられたアプリケーションで開くかを決定します。  

列挙型には、以下の事前定義された保存タイプが含まれています:  

|**タイプ**|**説明**|  
| :- | :- |  
|アタッチメント|スプレッドシートをブラウザに送り、.xls/.xlsx や他の拡張子に関連付けられたアプリケーションで添付ファイルとして開きます|  
|インライン|ドキュメントをブラウザに送り、スプレッドシートをディスクに保存するかブラウザ内で開くオプションを表示します|  

### **XLS ファイル**  

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

### **XLSX ファイル**  

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

### **PDF ファイル**  

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

### **注**  

Node.jsには標準のレスポンスオブジェクトが存在しないため、この機能はAspose.Cells for Node.js via C++にはありません。次のコードを参考にして、ストリームにファイルを保存し、その後ストリーム上で操作を行うことができます。  

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

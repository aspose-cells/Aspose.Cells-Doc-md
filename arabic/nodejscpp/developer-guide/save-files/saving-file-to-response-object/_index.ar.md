---  
title: حفظ الملف إلى كائن الرد باستخدام Node.js عبر C++  
linktitle: حفظ الملف في كائن الاستجابة  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/saving-file-to-response-object/  
description: تعلم كيفية إنشاء ملفات بشكل ديناميكي وإرسالها مباشرة إلى متصفح العميل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

تجعل Aspose.Cells من الممكن التلاعب بالملفات. يشرح هذا المقال الطرق المختلفة التي يمكن بواسطتها حفظ الملفات في كائن الاستجابة.  

{{% /alert %}}  

## **حفظ الملف في كائن الاستجابة**  

من الممكن أيضًا إنشاء ملف بشكل ديناميكي وإرسالها مباشرة إلى متصفح العميل. للقيام بذلك، استخدم نسخة محملة إضافية من طريقة [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) التي تقبل المعلمات التالية:  

- كائن استجابة Node.js.  
- اسم الملف.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/)، نوع إعلان المحتوى النوعي لملف الإخراج.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/)، نوع تنسيق الملف  

يحدد تعداد [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) ما إذا كان ملف الإرسال إلى المتصفح يوفر خيار الفتح مباشرة في المتصفح أو في تطبيق مرتبط بـ .xls/.xlsx أو امتداد آخر.  

يحتوي التعداد على أنواع الحفظ المحددة مسبقًا التالية:  

|**النوع**|**الوصف**|  
| :- | :- |  
|المرفقات|يُرسل جدول البيانات إلى المستعرض ويُفتح في تطبيق كمرفق مرتبط بامتداد .xls/.xlsx أو امتدادات أخرى|  
|مضمن|يُرسل المستند إلى المتصفح ويعرض خيارًا لحفظ جدول البيانات على القرص أو فتحه داخل المتصفح|  

### **ملفات XLS**  

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

### **ملفات XLSX**  

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

### **ملفات PDF**  

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

### **ملاحظة**  

نظرًا لغياب كائن استجابة معياري في Node.js، لا تتوفر هذه الوظيفة في Aspose.Cells for Node.js via C++. يمكنك الرجوع إلى الكود التالي لحفظ الملف على المجرى، ثم إجراء العمليات على المجرى.  

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

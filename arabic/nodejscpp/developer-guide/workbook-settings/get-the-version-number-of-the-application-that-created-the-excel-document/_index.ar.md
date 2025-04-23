---  
title: احصل على رقم إصدار التطبيق الذي أنشأ وثيقة Excel باستخدام Node.js عبر C++  
linktitle: الحصول على رقم الإصدار للتطبيق الذي أنشأ مستند Excel  
type: docs  
weight: 210  
url: /ar/nodejs-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/  
---  

{{% alert color="primary" %}}  

غالبًا ما تحتاج إلى معرفة رقم إصدار التطبيق الذي أنشأ وثيقة Microsoft Excel. توفر Aspose.Cells for Node.js via C++ خاصية [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--) لهذا الغرض.

{{% /alert %}}  

يوضح كود المثال التالي استخدام خاصية [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--)، حيث يحمل ملفات Excel التي أنشأتها Microsoft Excel 2003، 2007، 2010 و2013 ويطبع رقم إصدار التطبيق الذي أنشأ هذه الوثائق.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Print the version number of Excel 2003 XLS file
let workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2003.xls"));
console.log("Excel 2003 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2007 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2007.xls"));
console.log("Excel 2007 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2010 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2010.xls"));
console.log("Excel 2010 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2013 XLS file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2013.xls"));
console.log("Excel 2013 XLS Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2007 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2007.xlsx"));
console.log("Excel 2007 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2010 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2010.xlsx"));
console.log("Excel 2010 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());

// Print the version number of Excel 2013 XLSX file
workbook = new AsposeCells.Workbook(path.join(dataDir, "Excel2013.xlsx"));
console.log("Excel 2013 XLSX Version: " + workbook.getBuiltInDocumentProperties().getVersion());
```  


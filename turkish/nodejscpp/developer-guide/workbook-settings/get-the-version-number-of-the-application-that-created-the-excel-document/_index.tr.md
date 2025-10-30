---  
title: Node.js ve C++ kullanarak Oluşturan Uygulama Sürüm Numarasını Al  
linktitle: Excel Belgesini Oluşturan Uygulamanın Sürüm Numarasını Almak  
type: docs  
weight: 210  
url: /tr/nodejs-cpp/get-the-version-number-of-the-application-that-created-the-excel-document/  
---  

{{% alert color="primary" %}}  

Bir Microsoft Excel belgesini oluşturan uygulamanın sürüm numarasını bilmeniz gerekebilir. Aspose.Cells for Node.js via C++ bu amaçla [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--) özelliğini sağlar.

{{% /alert %}}  

Aşağıdaki örnek kod, [**Workbook.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getBuiltInDocumentProperties--) özelliğinin kullanımını gösterir. Microsoft Excel 2003, 2007, 2010 ve 2013 ile oluşturulan Excel dosyalarını yükler ve bu belgeleri oluşturan uygulamanın sürüm numarasını yazdırır.

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

{{< app/cells/assistant language="nodejs-cpp" >}}

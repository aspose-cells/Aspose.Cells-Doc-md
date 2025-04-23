---  
title: 在从HTML导入时避免大数字的指数表示  
linktitle: 在从HTML导入时避免大数字的指数表示  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: 学习如何在导入HTML时防止大数字被转换为指数表示法，使用Aspose.Cells for Node.js via C++。  
---  

{{% alert color="primary" %}}  

有时你的HTML中包含如1234567890123456这样超过15位的数字，当你将HTML导入到Excel文件中时，这些数字会被转换为指数记法，比如1.23457E+15。若你希望导入的数字保持原样，不被转换为指数记法，请在加载HTML时使用[**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--)属性并设置为**true**。  

{{% /alert %}}  

以下示例代码说明了[**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--)属性的用法。API将以原始形式导入数字，不进行指数转换。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Sample Html containing large number with digits greater than 15
const html = "<html><body><p>1234567890123456</p></body></html>";

// Convert Html to byte array
const byteArray = new TextEncoder().encode(html);

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setKeepPrecision(true);

// Convert byte array into stream
const stream = byteArray;

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output/");
workbook.save(path.join(outputDir, "outputAvoidExponentialNotationWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


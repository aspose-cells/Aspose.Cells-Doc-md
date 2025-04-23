---  
title: Json 通过 Node.js 与 C++ 实现  
linktitle: Json  
type: docs  
weight: 300  
url: /zh/nodejs-cpp/convert-workbook-to-json/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将 Excel 工作簿转换为 JSON。  
---  

{{% alert color="primary" %}}  
Aspose.Cells 支持将工作簿转换为 Json（JavaScript 对象表示法）文件。  
{{% /alert %}}  

## **将Excel工作簿转换为JSON**  

Aspose.Cells API 提供了将电子表格转换为 JSON 格式的支持。要导出工作簿到 JSON，请将 [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 作为 [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) 方法的第二个参数传递。你还可以使用 [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) 类来指定导出工作表到 JSON 的其他设置。  

以下代码示例演示如何使用 [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json) 枚举成员将活动工作表导出为 JSON。请参阅代码，将 [source file](book1.xlsx) 转换为 [输出 JSON 文件](book1.Json)。以作参考。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **高级主题**  
- [将CSV转换为JSON](/cells/zh/nodejs-cpp/convert-csv-to-json/)  
- [将Excel转换为JSON](/cells/zh/nodejs-cpp/convert-excel-to-json/)  
- [将JSON转换为CSV](/cells/zh/nodejs-cpp/convert-json-to-csv/)  
- [将JSON转换为Excel](/cells/zh/nodejs-cpp/convert-json-to-excel/)  


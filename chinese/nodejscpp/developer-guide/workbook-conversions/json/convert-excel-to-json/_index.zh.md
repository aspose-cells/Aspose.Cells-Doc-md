---  
title: 使用 Node.js 通过 C++ 转换 Excel 为 JSON  
linktitle: 转换Excel为JSON  
type: docs  
weight: 300  
url: /zh/nodejs-cpp/convert-excel-to-json/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将 Excel 文件转换为 JSON。  
keywords: 导出工作簿为 JSON，使用 C++ 实现。将 Excel 转换为 JSON ，适用于 Node.js  
---  

{{% alert color="primary" %}}  
Aspose.Cells 支持将工作簿转换为 JSON（JavaScript 对象表示法）文件。  
{{% /alert %}}  

## **将Excel工作簿转换为JSON**  

无需担心如何将 Excel 工作簿转换为 JSON，因为 Aspose.Cells for Node.js via C++ 库提供了最佳解决方案。Aspose.Cells API 支持将电子表格导出为 JSON 格式。要导出工作簿为 JSON，请将 [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) 作为 [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) 方法的第二个参数传递。你也可以使用 [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/) 类来指定导出工作表到 JSON 的其他设置。  

以下代码示例演示了导出 Excel 工作簿为 JSON。请查看此代码，将[源文件](sample.xlsx) 转换为由代码生成的 JSON 文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

以下代码示例使用 JsonSaveOptions 类来指定额外设置，并演示将Excel工作簿导出为JSON。请参考代码，将[源文件](sample.xlsx) 转换为由代码生成的JSON文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  



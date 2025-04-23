---  
title: 通过 C++ 使用 Node.js 将 JSON 转换为 CSV  
linktitle: 将JSON转换为CSV  
type: docs  
weight: 210  
url: /zh/nodejs-cpp/convert-json-to-csv/  
description: 学习如何使用Aspose.Cells for Node.js via C++将JSON数据转换为CSV。  
---  

## **将JSON转换为CSV**  

Aspose.Cells 支持将简单的JSON以及嵌套JSON转换为CSV。为此，API提供 [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) 类。[**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) 类提供JSON布局的选项，比如 [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--)（将数组作为表格处理）。[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) 类使用由 [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) 类设置的布局选项来处理JSON。  

 以下代码示例演示了如何使用 [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) 类加载 [源 JSON 文件](104398869.json)，并生成 [输出 CSV 文件](104398870.csv)。  

### **示例代码**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");


// Create sample JSON if missing
const jsonPath = path.join(sourceDir, "SampleJson.json");

// Read JSON file
const str = fs.readFileSync(jsonPath, "utf-8");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();

// Set JsonLayoutOptions
const importOptions = new AsposeCells.JsonLayoutOptions();
importOptions.setConvertNumericOrDate(true);
importOptions.setArrayAsTable(true);
importOptions.setIgnoreTitle(true);
AsposeCells.JsonUtility.importData(str, cells, 0, 0, importOptions);

// Save Workbook
workbook.save(outputDir + "SampleJson_out.csv");
```  


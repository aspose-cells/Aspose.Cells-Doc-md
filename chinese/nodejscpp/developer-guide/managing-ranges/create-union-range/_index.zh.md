---  
title: 使用Node.js via C++创建联合范围  
linktitle: 创建联合范围  
type: docs  
weight: 360  
url: /zh/nodejs-cpp/create-union-range/  
description: 学习如何使用Aspose.Cells for Node.js via C++创建联合范围。  
keywords: 使用Node.js via C++创建联合范围，联合范围Aspose.Cells Node.js，WorksheetCollection创建联合范围Node.js  
---  

## **创建联合范围**  
Aspose.Cells 提供了使用 [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) 方法创建联合范围的功能。该方法接受两个参数：创建联合范围的地址和工作表索引。调用此方法会返回一个 [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange)。  

以下代码片段演示了如何使用 [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) 方法创建联合范围，生成的输出文件已附上供参考。  

- [输出文件](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

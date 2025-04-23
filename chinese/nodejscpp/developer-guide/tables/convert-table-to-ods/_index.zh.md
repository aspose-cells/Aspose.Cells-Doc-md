---  
title: 将带有表格的Excel文件转换为ODS格式，使用Node.js与C++  
linktitle: 将表格转换为ODS  
type: docs  
weight: 70  
url: /zh/nodejs-cpp/convert-table-to-ods/  
description: 学习如何使用Aspose.Cells for Node.js via C++将Excel文件中的表转换为ODS格式。  
---  

Aspose.Cells支持将含有表格的Excel文件转换为ODS文件。只需将文件保存为ODS格式，生成的ODS文件内将包含可用的表格。

## 示例代码

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTable.xlsx"));

// Save the file
workbook.save(path.join(outputDir, "ConvertTableToOds_out.ods"));
```

示例代码生成的输出ODS文件已附上供您参考。

[**Output ODS File**](ConvertTableToOds_out.ods)  


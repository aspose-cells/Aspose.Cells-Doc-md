---  
title: Node.jsをC++経由で使用して、テーブルをODSに変換する  
linktitle: テーブルをODSに変換  
type: docs  
weight: 70  
url: /ja/nodejs-cpp/convert-table-to-ods/  
description: Aspose.Cells for Node.js via C++を使用して、テーブルを含むExcelファイルをODSフォーマットに変換する方法を学びます。  
---  

Aspose.Cellsは、テーブルを含むExcelファイルをODSファイルに変換することをサポートしています。ファイルをODS形式で保存すると、機能するテーブルを持つODSファイルが生成されます。

## サンプルコード

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

サンプルコードによって生成された出力ODSファイルが添付されています。

[**Output ODS File**](ConvertTableToOds_out.ods)  


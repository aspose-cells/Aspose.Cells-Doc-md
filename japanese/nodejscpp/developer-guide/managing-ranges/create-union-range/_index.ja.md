---  
title: Node.jsとC++を使ったユニオン範囲の作成方法  
linktitle: ユニオン範囲の作成  
type: docs  
weight: 360  
url: /ja/nodejs-cpp/create-union-range/  
description: Aspose.Cells for Node.js via C++を用いてユニオン範囲を作成する方法を学びます。  
keywords: Node.jsとC++を使用したユニオン範囲の作成方法、Aspose.Cellsのユニオン範囲作成、worksheetコレクションでの作成例  
---  

## **ユニオン範囲の作成**  
Aspose.Cellsは、[WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-)メソッドを使ってユニオン範囲を作成する機能を提供します。このメソッドは、ユニオン範囲を作成するアドレスとワークシートのインデックスの2つのパラメータを受け取ります。[WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-)は、[UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange)オブジェクトを返します。  

以下のコードスニペットは、[WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-)メソッドを使用してユニオン範囲を作成する例です。生成された出力ファイルは参考のために添付されています。  

- [出力ファイル](106364952.xlsx)  

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


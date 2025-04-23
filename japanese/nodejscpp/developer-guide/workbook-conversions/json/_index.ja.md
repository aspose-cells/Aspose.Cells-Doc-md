---  
title: Node.js経由でC++を使ったJSON  
linktitle: Json  
type: docs  
weight: 300  
url: /ja/nodejs-cpp/convert-workbook-to-json/  
description: Aspose.Cells for Node.js via C++を使用してExcelブックをJSONに変換する方法を学びます。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは、ワークブックをJson（JavaScript Object Notation）ファイルに変換することをサポートしています。  
{{% /alert %}}  

## **ExcelワークブックをJSONに変換**  

Aspose.Cells APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドの第2引数として[**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)を渡します。さらに、[**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions)クラスを使用してワークシートのエクスポート設定を追加で指定することも可能です。  

次のコード例では、[**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json)列挙型メンバーを使用してアクティブなワークシートをJSONにエクスポートする方法を示しています。ソースファイル（book1.xlsx）をコードで変換し、出力されるJsonファイル（book1.Json）を参照してください。  

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

## **高度なトピック**  
- [CSVをJSONに変換](/cells/ja/nodejs-cpp/convert-csv-to-json/)  
- [ExcelをJSONに変換する](/cells/ja/nodejs-cpp/convert-excel-to-json/)  
- [JSONをCSVに変換](/cells/ja/nodejs-cpp/convert-json-to-csv/)  
- [JSONをExcelに変換する](/cells/ja/nodejs-cpp/convert-json-to-excel/)  


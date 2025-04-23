---
title: Node.js経由でC++を使用してJSONをExcelに変換
linktitle: JSONをExcelに変換します。
type: docs
weight: 300
url: /ja/nodejs-cpp/convert-json-to-excel/
description: Aspose.Cells for Node.js via C++を使用してJSONをExcelファイルに変換する方法を学びましょう。
keywords: Office 2013、Office 2016、Office 2019、Office 365を使用せずにNode.js経由でC++を使ってJSONをインポートする方法。
---

{{% alert color="primary" %}}

Aspose.Cellsは、JSON（JavaScript Object Notation）ファイルをExcelブックに変換することをサポートしています。

{{% /alert %}}

## **JSONをExcelワークブックに変換する**
JSONをExcelファイルに変換する方法がわからなくても心配ありません。なぜなら、Aspose.Cells for Node.js via C++は最良のソリューションを提供しているからです。Aspose.CellsのAPIは、JSONフォーマットをスプレッドシートに変換するサポートを提供しています。[**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions)クラスを使用して、JSONをブックにインポートする追加設定を指定できます。

以下のコード例は、JSONをExcelワークブックにインポートする方法を示しています。コードで生成されたxlsxファイルへの変換のために、[source file](sample.json)を参照してください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

次のコード例は、JsonLoadOptionsクラスを使用して追加設定を指定し、JSONをExcelブックにインポートする例です。参考のため、ソースファイル([sample.json])をコードで変換し、生成されたxlsxファイルを確認してください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

次のコード例は、JSON文字列をExcelブックにインポートする例です。また、JSONをインポートするときのレイアウトの場所も指定できます。参考のため、JSON文字列をxlsxファイルに変換するコードを確認してください。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```

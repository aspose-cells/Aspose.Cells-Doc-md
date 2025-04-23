---
title: CSVをJSONに変換（Node.jsとC++経由）
linktitle: CSVをJSONに変換
type: docs
weight: 220
url: /ja/nodejs-cpp/convert-csv-to-json/
description: Aspose.Cells for Node.js via C++ APIを使用して、CSVファイルを簡単にJSONに変換します。
keywords: 変換、CSVをJSONに変換、CSVからJSONへ、CSV、JSON、CSVをJSONに変換（Node.jsとC++）
---

## **CSVをJSONに変換**

Aspose.Cellsでは、CSVをJSONに変換する機能がサポートされています。このために、APIは[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/)クラスを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)クラスはJSONへの範囲のエクスポートオプションを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)クラスには以下のプロパティがあります。

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): セルの文字列値をJSONにエクスポートします。
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--):範囲にヘッダー行が含まれているかどうかを示します。
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): インデントを示します。

この[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/)クラスは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)クラスで設定されたエクスポートオプションを使用してJSONをエクスポートします。

以下のコードサンプルは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/)クラスを使用して[ソースのCSVファイル](104398879.csv)をロードし、コンソールにJSON出力を出力する方法を示しています。

### **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Load CSV file
const filePath = path.join(sourceDir, "SampleCsv.csv");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);
const lastCell = workbook.getWorksheets().get(0).getCells().getLastCell();

// Set JsonSaveOptions
const jsonSaveOptions = new AsposeCells.JsonSaveOptions();
const range = workbook.getWorksheets().get(0).getCells().createRange(0, 0, lastCell.getRow() + 1, lastCell.getColumn() + 1);
const data = AsposeCells.JsonUtility.exportRangeToJson(range, jsonSaveOptions);

// Print JSON
console.log(data);
```

### **コンソール出力**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}

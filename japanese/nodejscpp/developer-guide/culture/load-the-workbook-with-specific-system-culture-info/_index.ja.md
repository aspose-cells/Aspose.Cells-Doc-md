---
title: System culture infoを指定してワークブックをロードするNode.jsとC++の例
linktitle: 特定のシステムカルチャ情報を使用してワークブックをロードする
type: docs
weight: 190
url: /ja/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **可能な使用シナリオ**
以前は特定の文化形式の数値と日付に対処するためにスレッド全体の文化情報を変更する必要がありましたが、今ではAspose.Cells for Node.js via C++が`LoadOptions.CultureInfo`プロパティを提供し、全体のスレッドの文化情報を変更せずにワークブックを特定の文化情報で読み込むことができます。

## **特定のシステムカルチャ情報を使用してワークブックをロードする**
以下のサンプルコードは、日付を処理するために特定のシステム文化情報を使ってワークブックをロードする方法を示しています。

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');

// Create a readable stream
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>10-01-2016</td></tr></table></body></html>");
inputStream.push(null); // Signal end of stream

const culture = new Intl.NumberFormat("en-GB", {
minimumFractionDigits: 2,
maximumFractionDigits: 2
```

以下のサンプルコードは、数値を処理するために特定のシステム文化情報を使ってワークブックをロードする方法を示しています。

```javascript
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');
const path = require("path");

const dataDir = path.join(__dirname, "data");
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>1234,56</td></tr></table></body></html>");
inputStream.push(null);

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Html);        
options.setRegion(AsposeCells.CountryCode.UnitedKingdom);

(async () => {
const workbook = new AsposeCells.Workbook(inputStream, options);
const cell = workbook.getWorksheets().get(0).getCells().get("A1");
console.assert(cell.getType() === AsposeCells.CellValueType.IsNumeric);
console.assert(cell.getDoubleValue() === 1234.56);
})();
```
{{< app/cells/assistant language="nodejs-cpp" >}}

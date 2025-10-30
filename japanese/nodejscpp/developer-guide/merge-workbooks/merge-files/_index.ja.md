---
title: Node.jsを使ったファイルのマージ
linktitle: ファイルの結合
type: docs
weight: 20
url: /ja/nodejs-cpp/merge-files/
---

## **紹介**

Aspose.Cellsはファイルのマージにさまざまな方法を提供しています。データ、書式設定、数式を含むシンプルなファイルには [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) 方法が複数のブックを結合するのに適しており、[**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) 方法はシートを新しいブックにコピーするのに適しています。これらの方法は使いやすく効果的ですが、多数のファイルをマージする場合、システムリソースを大量に使用することがあります。これを避けるために、より効率的な [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) 静的メソッドを使用します。

## **Aspose.Cells for Node.js via C++を使ったファイルのマージ**

以下のサンプルコードは、[**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) メソッドを使用して大きなファイルをマージする例です。Book1.xlsとBook2.xlsの2つの大きなファイルを対象とし、それらには書式設定済みのデータと数式のみが含まれています。

{{% alert color="primary" %}}

[**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-)メソッドは、データ、スタイル、書式、数式の結合のみをサポートしています。チャート、図、コメントなどのオブジェクトは、このメソッドを使用して結合することはできません。さらに、一時的なデータを処理するためのキャッシュファイルが使用されます。

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}

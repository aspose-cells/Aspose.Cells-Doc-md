---
title: Node.jsを使用してExcelをCSV、TSV、TXTに変換する
linktitle: CSV、TSV、TXTとして保存
type: docs
weight: 40
url: /ja/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells for Node.js via C++を使ったExcelファイルのCSV、TSV、TXTフォーマットへの変換方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、Excel、ODS、JSONなどのさまざまなフォーマットのファイルをCSV、TSV、TXTに変換できます。

{{% /alert %}}

## **ワークブックをテキストまたはCSV形式で保存**

複数のワークシートを持つワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式（例：TXT、TabDelim、CSVなど）の場合、デフォルトではMicrosoft ExcelとAspose.Cellsはアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法を説明します。ソースワークブックを読み込み、任意のMicrosoft ExcelまたはOpenOfficeのスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）に含まれる複数のワークシートを扱います。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正してファイルをCSV形式に保存することもできます。デフォルトでは、[**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--)はカンマなので、CSV形式で保存する場合はセパレータを指定しないでください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **カスタム区切り文字でテキストファイルを保存**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **高度なトピック**
- [CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する](/cells/ja/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。](/cells/ja/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}

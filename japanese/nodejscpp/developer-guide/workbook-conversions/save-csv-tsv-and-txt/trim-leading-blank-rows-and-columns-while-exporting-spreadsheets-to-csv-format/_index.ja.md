---
title: 先頭の空白行と列をトリムしながら Node.js を通じて C++ でスプレッドシートを CSV 形式にエクスポートする
linktitle: スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします
type: docs
weight: 100
url: /ja/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for Node.js via C++ を使用して、スプレッドシートを CSV 形式にエクスポートするときに先頭の空白行と列をトリムする方法を学びます。
---

## **可能な使用シナリオ**

ExcelまたはCSVファイルには先行する空白の列または行が含まれている場合があります。 たとえば、この行を考えてみてください

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の3つのセルまたは列が空白です。 このようなCSVファイルをMicrosoft Excelで開くと、Microsoft Excelはこれらの先行する空白行と列を破棄します。

デフォルトでは、Aspose.Cells for Node.js via C++ は保存時に先頭の空白列と行を破棄しませんが、Microsoft Excel のように削除したい場合は、Aspose.Cells は [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) プロパティを提供します。これを **true** に設定すると、保存時にすべての先頭の空白行と列が破棄されます。

{{% alert color="primary" %}}

リリース Aspose.Cells for Node.js via C++ 20.4 以前は、[**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) の既定値は **false** でした。20.4 リリース以降、[**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) の既定値は **true** となっています。

{{% /alert %}}

## **スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。**

以下のサンプルコードは、先頭に空白列が二つある [ソース excel ファイル](sampleTrimBlankColumns.xlsx) を読み込みます。最初は変更なしで CSV 形式で保存し、その後 [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) プロパティを **true** に設定して再保存します。スクリーンショットは、[ソース excel ファイル](sampleTrimBlankColumns.xlsx)、トリミングなしの [出力 CSV ファイル](outputWithoutTrimBlankColumns.csv)、およびトリミング後の [出力 CSV ファイル](outputTrimBlankColumns.csv) を示しています。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```

---
title: Node.js経由でC++を使用してExcelの読み込み時にVBAプロジェクトをフィルタリングする方法
linktitle: ワークブックを読み込む際にVBAプロジェクトをフィルタリングする
type: docs
weight: 140
url: /ja/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Aspose.Cells for Node.js via C++を使用してExcelブックを読み込む際にVBAプロジェクトをフィルタリングする方法を学びます。
---

## **Node.js経由でC++を使用してExcelの読み込み時にVBAプロジェクトをフィルタリングする**

一部の.xlsm/.xslbファイルには、非常に大量のマクロ（または非常に長いマクロ）が含まれています。Aspose.Cells for Node.js via C++は、そのようなブックを開くときに無条件でこれらのメタデータをロードします。ただし、大量のブックのシート名だけを抽出する必要がある場合は、[**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions)を使用してこの処理を制御し、不要な内容をスキップできます。このフィルターは、新しいオプション、[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions)を導入することで提供されます。

## **サンプルコード**

以下のサンプルコードは、VBAのみがフィルタリングされたワークブックを読み込みます。この機能のテスト用に使用されるサンプルファイルを提供するリンクがあります。

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Node.js経由でC++を使ってODF 1.1、1.2、1.3形式で保存
linktitle: ODF 1.1、1.2、1.3でODSファイルを保存
description: ExcelをODF 1.1、1.2および1.3仕様に変換する方法をAspose.Cells for Node.js via C++で学びます。
type: docs
weight: 230
url: /ja/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ODSファイル（**OpenDocument Spreadsheet**）をODF（**OpenDocument Format**）1.1、1.2、1.3仕様で保存することをサポートしています。Aspose.Cellsには[**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--)プロパティがあり、ODSファイルの保存時に使用するODFバージョンを指定します。このプロパティのデフォルト値は[**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/)であり、この設定なしで保存されたODSファイルは1.2仕様を使用します。

{{% /alert %}}

以下のサンプルコードは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1に値を追加し、その後ODF 1.1、1.2、1.3仕様でODSファイルを保存する例です。デフォルトでは、ODSファイルはODF 1.2仕様で保存されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```

---
title: Node.js を通じて C++ で複数エンコーディングの CSV ファイルを読み取る
linktitle: 複数のエンコーディングでのCSVファイルの読み込み
type: docs
weight: 200
url: /ja/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: 複数のエンコーディング（Unicode、ANSI、UTF8、UTF7 など）を持つ CSV ファイルの読み取り方法を Aspose.Cells for Node.js via C++ で学習します。
---


{{% alert color="primary" %}}

時には、CSV ファイルが複数のエンコーディング（Unicode、ANSI、UTF8、UTF7 など）を含む場合があります。Aspose.Cells を使えば、そのようなCSVファイルを正しく読み込み、他のフォーマット（PDFや XLSX など）に変換できます。

{{% /alert %}}

Aspose.Cellsは[**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--)プロパティを提供しており、これを**true**に設定する必要があります。そうすることで、複数エンコーディングのCSVファイルを正しく読み込むことができます。

以下のスクリーンショットは、2行を含むサンプルCSVファイルを示しています。1行目は**ANSI**エンコーディングで、2行目は**Unicode**エンコーディングです

|**入力ファイル**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下のスクリーンショットは、上記のCSVファイルから変換されたXLSXファイルを、[**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--)プロパティを**true**に設定しなかった場合を示しています。ご覧のとおり、Unicodeテキストは正しく変換されませんでした。

|**出力ファイル1: 複数のエンコーディングを考慮していない**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下のスクリーンショットは、[**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) プロパティを **true** に設定した後、上記 CSV ファイルから変換された XLSX ファイルです。Unicode テキストは正しく変換されました。

|**出力ファイル2: IsMultiEncodedをtrueに設定**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記のCSVファイルを正しくXLSX形式に変換するサンプルコードです。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## 関連記事

- [CSV ファイルを開く](/cells/ja/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)

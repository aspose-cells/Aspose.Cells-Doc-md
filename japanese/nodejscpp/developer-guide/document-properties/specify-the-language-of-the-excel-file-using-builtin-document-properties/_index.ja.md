---
title: BuiltInドキュメントプロパティを使用してExcelファイルの言語を指定（Node.jsとC++）
linktitle: ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する
type: docs
weight: 30
url: /ja/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **可能な使用シナリオ**

Excelファイルの言語を変更するには、ファイルを右クリックし、プロパティ > 詳細設定を選択し、言語フィールドを編集します。プログラムから変更するには、[**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) プロパティを利用し、Aspose.Cells for Node.js via C++ APIを使用してください。

## **ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する**

このコードは、ワークブックを作成し、その組み込みドキュメントプロパティである言語を変更します。コードで生成されたExcelファイルと修正された言語フィールドのスクリーンショットは[**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--)プロパティによります。

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object.
const wb = new AsposeCells.Workbook();

// Access built-in document property collection.
const bdpc = wb.getBuiltInDocumentProperties();

// Set the language of the Excel file.
bdpc.setLanguage("German, French");

// Save the workbook in xlsx format.
wb.save(path.join(outputDir, "outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

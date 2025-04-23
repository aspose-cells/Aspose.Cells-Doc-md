---
title: Node.jsとC++を使用したWord Artテキストの組み込みスタイルの追加
linktitle: 組み込みスタイルを持つ WordArt テキストを追加する
type: docs
weight: 270
url: /ja/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: Aspose.Cells for Node.js via C++を使用したWord Artテキストの追加と組み込みスタイルの適用方法を学び、Excel内で視覚的に魅力的なテキストを作成します。
---

## **可能な使用シナリオ**
Aspose.Cells for Node.js via C++を使用してWord Artテキストを追加し、組み込みスタイルを適用できます。これには [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) メソッドを使用してください。

## **組み込みスタイルを持つ WordArt テキストを追加する**
以下のサンプルコードは、異なる組み込みスタイルのワードアートテキストを追加します。このコードで生成された[output excel file](5115470.xlsx)をチェックしてください。これがMicrosoft Excelで表示される[output excel file](5115470.xlsx)の外観です。

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add Word Art Text with Built-in Styles
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```

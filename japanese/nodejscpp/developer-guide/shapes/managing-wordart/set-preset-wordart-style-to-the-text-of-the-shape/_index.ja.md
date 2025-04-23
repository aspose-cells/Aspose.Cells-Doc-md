---
title: Node.jsを使用して図形のテキストにプリセットWordArtスタイルを設定
linktitle: シェイプのグローエフェクトの色を読み取る
type: docs
weight: 280
url: /ja/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: ユースケースとして、Aspose.Cells for Node.js via C++を使用して図形のテキストにプリセットWordArtスタイルを設定する方法を学ぶ
---

## **可能な使用シナリオ**
Aspose.Cells for Node.js via C++を使用して図形のテキストにプリセットWordArtスタイルを設定できます。これには [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) もしくは [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) を使用してください。

## **テキストのシェイプに組み込みのWordArtスタイルを設定する**
次のサンプルコードは、テキストを含むテキストボックスを作成し、そのテキストのプリセットWordArtスタイルを [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) メソッドを使用して設定します。これにより、出力されるExcelファイルの見た目はMicrosoft Excelで次の通りです：

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a textbox with some text
const textbox = worksheet.getShapes().addTextBox(0, 0, 0, 0, 100, 700);
textbox.setText("Aspose File Format APIs");
textbox.getFont().setSize(44);

// Sets preset WordArt style to the text of the shape.
const fntSetting = textbox.getRichFormattings()[0];
fntSetting.setWordArtStyle(AsposeCells.PresetWordArtStyle.WordArtStyle3);

// Save the workbook in xlsx format
workbook.save(outputDir + "outputSetPresetWordArtStyle.xlsx");
```

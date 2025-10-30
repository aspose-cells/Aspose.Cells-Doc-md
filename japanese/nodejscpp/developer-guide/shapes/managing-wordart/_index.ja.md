---
title: Node.jsとC++を使ったワークシートへのWordArtウォーターマークの追加
linktitle: ワードアートの管理
type: docs
weight: 180
url: /ja/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Aspose.Cells for Node.js via C++を使って、ワークシートに背景ウォーターマークとしてWordArtを追加する方法を学びます。
---

{{% alert color="primary" %}} 

WordArtを使用してスプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルをファイルの上に広げたり、テキストを装飾したり、テキストをプリセットの形状に合わせたり、Excelシートにテキストを背景ウォーターマークとして適用したりできます。WordArtは、スプレッドシートに追加するための移動や配置が可能なオブジェクトになります。

{{% /alert %}} 

次の例では、ワークシートの背景ウォーターマークとしてワードアート形状を追加する方法を示します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();            

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
const lineFormat = wordart.getLine();          

const outputFilePath = path.join(dataDir, "Watermark_Test.out.xls");
// Save the file
workbook.save(outputFilePath);
```

## **高度なトピック**
- [組み込みスタイルを持つ WordArt テキストを追加する](/cells/ja/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [WordArtウォーターマークをロックする](/cells/ja/nodejs-cpp/locking-wordart-watermark/)
- [テキストのシェイプに組み込みのWordArtスタイルを設定する](/cells/ja/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="nodejs-cpp" >}}

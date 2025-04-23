---  
title: Node.jsを使用してWordArtウォーターマークのロック  
linktitle: WordArtウォーターマークをロックする  
type: docs  
weight: 170  
url: /ja/nodejs-cpp/locking-wordart-watermark/  
description: Aspose.Cells for Node.js via C++でWordArtウォーターマークをロックする方法を学ぶ  
---  

{{% alert color="primary" %}}  

Aspose.CellsのAPIは、ワークシート上にWordArtウォーターマークを追加し、移動や配置が可能なオブジェクトとして扱えるようにします。また、編集や移動・選択のためにWordArtオブジェクトをロックすることも可能です。この記事は、特定の[**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-)メソッドを使用してウォーターマークの一部の側面をロックする方法を説明します。

{{% /alert %}}  

Aspose.CellsのAPIは、ユーザーの操作を制限または完全にブロックできるよう、ウォーターマークの特定の側面をロックします。以下のコードスニペットは、nullからスプレッドシートを作成し、Aspose.Cells for Node.js via C++を使用してウォーターマークの選択、移動、編集、およびリサイズをロックする方法を示しています。  

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

// Lock Shape Aspects
wordart.setIsLocked(true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Selection, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.ShapeType, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Move, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Resize, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Text, true);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();

// Set the color
wordArtFormat.setOneColorGradient(AsposeCells.Color.Red, 0.2, AsposeCells.GradientStyleType.Horizontal, 2);

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
wordart.setHasLine(false);

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  


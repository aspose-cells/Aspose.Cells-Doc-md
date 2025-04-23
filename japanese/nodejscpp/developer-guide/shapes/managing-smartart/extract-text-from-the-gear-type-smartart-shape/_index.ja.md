---
title: Node.js経由でC++を使用してGearタイプのSmartArt Shapeからテキスト抽出
linktitle: ギア型スマートアート形状からテキストを抽出
type: docs
weight: 500
url: /ja/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aspose.Cells for Node.js via C++を使用してGearタイプのSmartArt Shapeからテキストを抽出する方法を学びます。
---

## **可能な使用シナリオ**

Aspose.CellsはGearタイプのSmart Art Shapeからテキストを抽出できます。最初にSmart Art Shapeを[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--)メソッドを使用してグループシェイプに変換し、その後、[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--)メソッドを用いてグループシェイプを構成する個々のシェイプの配列を取得します。最後にループを使ってすべての個々のシェイプからテキストを抽出します。

## **ギアタイプのスマートアートシェイプからテキストを抽出する**

以下のサンプルコードは、上記で説明したように、Gear Type Smart Art Shapeを含む[sample Excel file](67338483.xlsx)をロードし、その個々の形状からテキストを抽出します。以下は、サンプルコードのコンソール出力です。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **コンソール出力**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}

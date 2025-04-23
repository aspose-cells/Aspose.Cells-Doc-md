---
title: Shapeのグロウ効果の色をNode.jsとC++を使用して読み取る
linktitle: 形状のグローエフェクトの色を読み取りたい場合は、{0}プロパティを使用してください。これにより、形状のグローエフェクトの色に関連するさまざまなプロパティがわかります。
type: docs
weight: 330
url: /ja/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Aspose.Cells for Node.js via C++を使用して、シェイプの輝き効果の色を読む方法を学びます。 
---

## 可能な使用シナリオ

任意のシェイプの輝き効果の色を読みたい場合は、[**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)プロパティを使用してください。これにより、シェイプの輝き効果に関連するさまざまなプロパティを見つけるのに役立ちます。

## シェイプのグローエフェクトの色を読む

参照のために、以下はサンプルコードとその [ソースエクセルファイル](22774108.xlsx) およびコンソール出力を示したスクリーンショットです。次のスクリーンショットは、Microsoft Excelで表示したときのソースエクセルファイル内の形状のグローエフェクトを示しています。

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Node.jsを使用したシェイプの輝き効果の色を読むコード例

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Read the source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sourceGlowEffectColor.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the shape
const shape = sheet.getShapes().get(0);

// Read the glow effect color and its various properties
const effect = shape.getGlow();
const color = effect.getColor();
console.log("Color: " + color.getColor());
console.log("ColorIndex: " + color.getColorIndex());
console.log("IsShapeColor: " + color.isShapeColor());
console.log("Transparency: " + color.getTransparency());
console.log("Type: " + color.getType());
```

## コンソール出力

提供された [ソースエクセルファイル](22774108.xlsx) で上記のサンプルコードを実行したときのコンソール出力は次のとおりです。

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}

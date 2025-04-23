---
title: C++経由のNode.jsを使ったシェイプまたはチャートの反射効果の操作
linktitle: 図形またはグラフの反射効果の操作
type: docs
weight: 210
url: /ja/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Aspose.Cells for Node.js via C++を使用して、シェイプまたはチャートの反射効果の操作方法を学び、さまざまな反射プロパティを設定して望ましい結果を得ます。
---

## **可能な使用シナリオ**
Aspose.Cells for Node.js via C++は、[Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--)プロパティと[ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect)クラスを提供し、シェイプやチャートの反射効果を操作できます。[ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect)クラスは、さまざまな結果を得るために設定可能な以下のプロパティを含みます。

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **図形またはグラフの反射効果の操作**
以下のサンプルコードは、[ソースExcelファイル](5115424.xlsx)を読み込み、デフォルトワークシートの最初のシェイプにアクセスし、[Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--)クラスのさまざまなプロパティを設定し、その後ワークブックを[出力Excelファイル](5115423.xlsx)に保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

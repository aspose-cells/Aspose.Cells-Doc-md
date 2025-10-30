---  
title: C++経由のNode.jsを使ったシェイプまたはチャートの輝き効果の操作  
linktitle: 形状またはチャートのグローエフェクトの操作  
type: docs  
weight: 240  
url: /ja/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Aspose.Cells for Node.js via C++を使用して、シェイプまたはチャートの輝き効果の操作方法を学びます。  
---  

## **可能な使用シナリオ**  
Aspose.Cellsは、[Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--)プロパティと[GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/)クラスを提供しており、シェイプやチャートの輝き効果を操作できます。[GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/)クラスは、さまざまな結果を得るために設定できる以下のプロパティを含んでいます。  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **形状またはチャートのグローエフェクトの操作**  
以下のサンプルコードは、[ソースExcelファイル](5115407.xlsx)を読み込み、最初のワークシートの最初のシェイプにアクセスし、[Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--)プロパティのサブプロパティを設定し、その後ワークブックを[出力Excelファイル](5115414.xlsx)に保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}

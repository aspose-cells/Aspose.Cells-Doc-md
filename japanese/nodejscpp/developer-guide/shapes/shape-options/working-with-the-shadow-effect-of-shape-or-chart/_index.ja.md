---  
title: C++経由のNode.jsを使ったシェイプまたはチャートのシャドウ効果の操作  
linktitle: 図形またはグラフの影効果の操作  
type: docs  
weight: 220  
url: /ja/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Aspose.Cells for Node.js via C++を使用して、シェイプやチャートのシャドウ効果の操作方法を学びます。  
---  

## **可能な使用シナリオ**  
Aspose.Cells for Node.js via C++は、[Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--)プロパティと[ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect)クラスを提供し、シェイプやチャートのシャドウ効果を操作します。[ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect)クラスは、さまざまな結果を得るために設定可能な以下のプロパティを含みます。  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **図形またはグラフの影効果の操作**  
次のサンプルコードは、[ソースExcelファイル](5115425.xlsx)をロードし、最初のワークシートの最初の図形にアクセスし、[Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) プロパティのサブプロパティを設定し、その後ワークブックを保存し、[出力Excelファイル](5115411.xlsx)として保存します。  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  


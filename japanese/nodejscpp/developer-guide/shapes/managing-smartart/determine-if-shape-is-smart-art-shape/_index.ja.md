---  
title: Node.js経由でC++を使用してShapeがスマートアートシェイプかどうかを判定  
linktitle: 形状がスマートアート形状かどうかの判定  
type: docs  
weight: 400  
url: /ja/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Aspose.Cells for Node.js via C++を使ってExcelのShapeがスマートアートシェイプかどうかを判定する方法を学びます。  
---  

## **可能な使用シナリオ**  

スマートアートシェイプは、Microsoft Excelの特殊なシェイプで、自動的に複雑な図を作成できます。Shapeがスマートアートか通常のシェイプかどうかは[**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--)プロパティを使って調査できます。  

## **シェイプがスマートアートシェイプかどうかを判定する**  

次のサンプルコードは、[サンプルExcelファイル](55541792.xlsx)を読み込み、このスクリーンショットのようにスマートアートシェイプを含みます。その後、最初のシェイプの[**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--)プロパティの値を出力します。以下にそのコンソール出力例を示します。  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **コンソール出力**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  


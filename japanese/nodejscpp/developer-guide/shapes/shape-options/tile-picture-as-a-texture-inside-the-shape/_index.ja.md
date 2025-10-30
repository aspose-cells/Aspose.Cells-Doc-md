---  
title: C++経由でNode.js内のシェイプにテクスチャとしてタイル貼りした画像を使用する  
linktitle: シェイプ内のテクスチャとして画像をタイル状に配置  
type: docs  
weight: 1700  
url: /ja/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Aspose.Cells for Node.js via C++を使用して、シェイプ内に小さな画像をテクスチャとしてタイル貼りする方法を学びます。  
---  

## **可能な使用シナリオ**  

画像が小さく、品質を失うことなく形状の全体の表面をカバーしない場合、タイリングするオプションがあります。タイリングは、タイルであるかのように小さな画像で形状の表面を埋めるものです。  

## **画像を形状の内部にテクスチャとしてタイル状にする**  

画像をシェイプの表面に塗りつけて、[**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--)プロパティをtrueに設定してタイル貼りできます。以下のサンプルコードと、それに付随する[サンプルExcelファイル](46465050.xlsx)およびスクリーンショットを参照してください。  

## **スクリーンショット**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

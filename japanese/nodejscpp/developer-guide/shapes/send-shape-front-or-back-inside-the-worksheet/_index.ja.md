---
title: Node.jsとC++を使ってワークシート内のシェイプを前面または背面に送る
linktitle: ワークシート内でShape FrontまたはBackを送信する
type: docs
weight: 3400
url: /ja/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++を使用して、ワークシート内の図形を前面または背面に送る方法を学びます。 
---

## **可能な使用シナリオ**

同じ場所に複数の図形が存在する場合、それらの可視性はz順序の位置によって決まります。Aspose.Cellsは [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-) メソッドを提供しており、これにより図形のz順序の位置を変更できます。図形を背面に送るには-1、-2、-3などの負の数を使用し、前面に持ち上げるには1、2、3などの正の数を使用します。

## **ワークシート内でShape FrontまたはBackを送信する**

次のサンプルコードは、[**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-)メソッドの使用例を説明しています。コード内で使用されている[サンプルExcelファイル](50528330.xlsx)と、その出力として生成された[Excelファイル](50528331.xlsx)を参照してください。このコード実行時のサンプルExcelファイルへの効果を示したスクリーンショットもあります。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```

---  
title: ワークシート内のコメントやShapeの余白設定をNode.jsとC++で行う  
linktitle: ワークシート内のコメントまたは図形の余白を設定する  
type: docs  
weight: 1500  
url: /ja/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Aspose.Cells for Node.js via C++を使用して、Excelワークシート内のコメントやShapeの余白を設定する方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.Cellsでは、[**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/) プロパティを使用して、任意のShapeまたはコメントの余白を設定できます。このプロパティは [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment) クラスのオブジェクトを返し、上部、左、下、右の余白を設定するためにさまざまなプロパティ（例：[**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--)、[**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--)、[**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--)、[**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--)）を持ちます。  

## **ワークシート内のコメントまたは図形の余白を設定する**  

次のサンプルコードをご覧ください。二つの図形を含む[サンプルエクセルファイル](61767851.xlsx)をロードし、コードでそれぞれの図形にアクセスし、それらの上部、左側、下部、右側の余白を設定します。コードによって生成された[出力エクセルファイル](61767852.xlsx)と、出力エクセルファイルに対するコードの効果を示したスクリーンショットをご覧ください。  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  


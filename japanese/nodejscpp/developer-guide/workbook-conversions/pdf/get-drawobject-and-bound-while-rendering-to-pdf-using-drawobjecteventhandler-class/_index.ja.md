---
title: DrawObjectEventHandlerクラスを使用して、ノード.js経由でC++で描画中のDrawObjectとBoundを取得する
linktitle: DrawObjectEventHandler クラスを使用して PDF にレンダリングする際の DrawObject および Bound を取得
type: docs
weight: 70
url: /ja/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能な使用シナリオ**

Aspose.Cellsは、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)という抽象クラスを提供し、[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)メソッドを持ちます。ユーザーは[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)を実装し、ExcelをPDFまたは画像にレンダリングする際に[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)メソッドを利用して[**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)とBoundを取得できます。以下は[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)メソッドのパラメータの概要です。

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)はレンダリング時に初期化され返されます。

- x: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)の左端。

- y: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)の上端。

- width: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)の幅。

- height: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)の高さ。

ExcelファイルをPDFへレンダリングする場合、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)クラスと[**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--)を利用できます。同様に、Excelファイルを画像にレンダリングする場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)クラスと[**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--)を利用できます。

## **DrawObjectEventHandlerクラスを使用してPDFへのレンダリング中にDrawObjectとバインドを取得**

次のサンプルコードを参照してください。これは、サンプルExcelファイル（[64716821.xlsx]）を読み込み、[出力PDF](64716822.pdf)として保存します。PDFへのレンダリング中に、[**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--)プロパティを利用し、既存のセルや画像などのオブジェクトの[**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)とBoundを取得します。[**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)タイプがCellの場合、BoundとStringValueを出力します。[**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)タイプがImageの場合、BoundとShape Nameを出力します。詳細は以下のサンプルコードのコンソール出力をご参照ください。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");

class ClsDrawObjectEventHandler extends AsposeCells.DrawObjectEventHandler {
draw(drawObject, x, y, width, height) {
console.log("");

// Print the coordinates and the value of Cell object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Cell) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.getCell().getStringValue()}`);
}

// Print the coordinates and the shape name of Image object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Image) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Shape Name]: ${drawObject.getShape().getName()}`);
}

console.log("----------------------");
}
}

async function run() {
// Load sample Excel file
const workbook = new AsposeCells.Workbook("sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");

// Specify Pdf save options
const opts = new AsposeCells.PdfSaveOptions();

// Assign the instance of DrawObjectEventHandler class
opts.setDrawObjectEventHandler(new ClsDrawObjectEventHandler());

// Save to Pdf format with Pdf save options
await workbook.saveAsync("outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

run();
```

## **コンソール出力**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}

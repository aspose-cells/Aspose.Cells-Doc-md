---
title: Node.js経由でC++を使用してセル参照に基づく画像を挿入
linktitle: セル参照に基づいて画像を挿入する
type: docs
weight: 150
url: /ja/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Aspose.Cells for Node.js via C++を使用して、セル参照に基づいてワークシートに画像を挿入する方法を学びます。セルのデータを画像内に表示させることができます。
---

{{% alert color="primary" %}}
時々、空の画像があり、Formula Barでセル参照を設定して画像内のデータや内容を表示する必要があります。 Aspose.Cellsはこの機能（Microsoft Excel 2010）をサポートしています。
{{% /alert %}}

## セル参照に基づいて画像を挿入する

Aspose.Cells for Node.js via C++は、ワークシートのセルの内容を画像形状に表示することをサポートします。表示したいデータを含むセルへのリンクを作成できます。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、そのセルやセル範囲のデータを変更すると、変更内容が自動的にグラフィックオブジェクトに反映されます。[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection)コレクションの[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)メソッドを呼び出して、ワークシートに画像を追加します。セル範囲は[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture)オブジェクトの[**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--)属性を使用して指定します。

### コード例

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```

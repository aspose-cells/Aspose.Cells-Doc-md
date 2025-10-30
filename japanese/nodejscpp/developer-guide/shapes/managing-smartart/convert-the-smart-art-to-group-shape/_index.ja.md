---
title: Node.js経由でC++を使用してスマートアートをグループシェイプに変換
linktitle: スマートアートをグループ形状に変換
type: docs
weight: 200
url: /ja/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **可能な使用シナリオ**

 [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--)メソッドを使用して、スマートアートシェイプをグループシェイプに変換できます。これにより、スマートアートシェイプをグループシェイプのように扱うことができ、個々の一部分やシェイプにアクセスできるようになります。

## **スマートアートをグループシェイプに変換する**

次のサンプルコードは、[サンプルExcelファイル](55541793.xlsx)を読み込み、このスクリーンショットのようにスマートアートシェイプを含みます。その後、スマートアートシェイプをグループシェイプに変換し、Shape.isGroupプロパティを出力します。以下にそのコンソール出力例を示します。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **コンソール出力**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}

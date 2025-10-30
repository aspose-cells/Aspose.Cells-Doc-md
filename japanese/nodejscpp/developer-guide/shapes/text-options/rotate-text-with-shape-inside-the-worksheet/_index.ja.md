---
title: 워크シート内のShapeでテキストを回転させる方法をNode.jsとC++で学ぶ
linktitle: ワークシート内の図形と一緒にテキストを回転する
type: docs
weight: 1300
url: /ja/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++を使用して、Excelワークシート内のShapeとともにテキストを回転させる方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelを使用して任意のシェイプ内にテキストを追加できます。非常に古いMicrosoft Excel 2003を使用してシェイプを追加すると、テキストはシェイプと一緒に回転しません。ただし、Microsoft Excelの新しいバージョン（例：2007、2010、2013、2016など）を使用してシェイプを追加すると、テキストはシェイプと共に回転します。テキストがシェイプと一緒に回転すべきかどうかを制御するには、[**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) プロパティを使用します。初期値は **true** で、これはテキストがシェイプとともに回転することを意味しますが、**false** に設定すると、テキストはシェイプとともに回転しません。

## **ワークシート内の図形と一緒にテキストを回転する**

次のサンプルコードは、三角形のシェイプとそのテキストがシェイプとともに回転するサンプルExcelファイル([sample Excel file](64716896.xlsx))をロードします。Microsoft ExcelでサンプルExcelファイルを開き、三角形のシェイプを回転させると、テキストもそれに伴い回転します。次に、[**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) プロパティを **false** に設定し、[出力Excelファイル](64716897.xlsx)として保存します。これにより、Microsoft Excelで出力ファイルを開き三角形を回転させても、テキストは回転しません。サンプルExcelファイルに対するこのコードの効果のスクリーンショットを参照してください。

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

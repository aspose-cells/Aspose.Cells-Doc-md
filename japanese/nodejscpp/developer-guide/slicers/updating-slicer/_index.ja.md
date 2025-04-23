---
title: Node.js経由のC++を用いたスライサー更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/nodejs-cpp/updating-slicer/
description: この記事は、Aspose.Cells for Node.js via C++を使用してスライサーを更新することでリンクされたピボットテーブルを更新する方法を示しています。
keywords: Aspose.Cells Node.jsをC++経由で、Node.jsのスライサーを更新する方法、Node.jsでスライサーを変更する方法、Node.jsでスライサーを調整する方法、Node.jsをC++経由でスライサーアイテムを選択または選択解除する方法。
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーを更新したい場合は、そのアイテムを選択または選択解除し、それに応じてスライサーテーブルまたはピボットテーブルが更新されます。Aspose.Cellsを使用してスライサーアイテムを選択または選択解除し、その後[**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--)を呼び出してスライサーまたはピボットテーブルを更新してください。

## **スライサーの更新方法**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](67338475.xlsx) を読み込みます。スライサーの2番目と3番目の項目を選択解除し、スライサーを更新します。それからワークブックを[出力Excelファイル](67338476.xlsx)として保存します。スクリーンショットには、サンプルコードがサンプルExcelファイルに与えた影響が示されています。スクリーンショットでは、選択された項目を持つスライサーを更新することでピボットテーブルも更新されていることがわかります。

![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```

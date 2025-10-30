---
title: Node.jsをC++経由でスライサーを削除
linktitle: スライサーの削除
type: docs
weight: 30
url: /ja/nodejs-cpp/removing-slicer/
---

## **可能な使用シナリオ**

Excelでスライサーを削除したい場合は、それを選択して *Delete* ボタンを押してください。同様に、Aspose.Cells APIを使用してプログラム的に削除したい場合は、 [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-) メソッドを使用します。これにより、ワークシートからスライサーが削除されます。

## **スライサーの削除**

以下のサンプルコードは既存のスライサーを含む[サンプルExcelファイル](67338478.xlsx)を読み込み、スライサーにアクセスして削除し、最後に[出力Excelファイル](67338477.xlsx)として保存します。スクリーンショットは、実行後に削除されるスライサーを示しています。

![todo:image_alt_text](removing-slicer_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

---
title: Nothing to printがあるときに空白ページを出力する（Node.js経由でC++使用）
linktitle: 空白ページを出力する。印刷するものがない場合
type: docs
weight: 90
url: /ja/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **可能な使用シナリオ**

シートが空の場合、Aspose.Cellsは何も印刷しません。この挙動を変更するには、[**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--)プロパティを使用します。これを**true**に設定すると、空白ページが印刷されます。

## **印刷するものがない場合、空白ページを出力**

以下のサンプルコードは、空のワークブックと空のワークシートを作成し、[**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--)プロパティを**true**に設定した後、空のワークシートを画像にレンダリングします。その結果、何も印刷するものがないため空白ページが生成されます。これは以下の画像で確認できます。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```

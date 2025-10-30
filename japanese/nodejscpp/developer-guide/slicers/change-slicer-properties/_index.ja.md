---
title: スライサーのプロパティをNode.jsをC++経由で変更
linktitle: スライサープロパティを変更する
type: docs
weight: 70
url: /ja/nodejs-cpp/change-slicer-properties/
---

## **可能な使用シナリオ**

配置や行の高さなど、スライサーのプロパティを変更したい場合があります。Aspose.Cells for Node.js via C++はこれらのプロパティを更新するオプションを提供します。

## **スライサープロパティを変更する**

次のサンプルコードをご覧ください。最初の列を含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込み、その後、高さ、幅、印刷可能、タイトルなどのプロパティを変更したスライサーを作成します。ワークブックを[outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx)として保存します。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing a table.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateSlicerToExcelTable.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first table inside the worksheet.
const table = worksheet.getListObjects().get(0);

// Add slicer
const idx = worksheet.getSlicers().add(table, 0, "H5");

const slicer = worksheet.getSlicers().get(idx);
slicer.setPlacement(AsposeCells.PlacementType.FreeFloating);
slicer.setRowHeightPixel(50);
slicer.setWidthPixel(500);
slicer.setTitle("Aspose");
slicer.setAlternativeText("Alternate Text");
slicer.setIsPrintable(false);
slicer.setIsLocked(false);

// Refresh the slicer.
slicer.refresh();

// Save the workbook in output XLSX format.
workbook.save(path.join(outputDir, "outputChangeSlicerProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

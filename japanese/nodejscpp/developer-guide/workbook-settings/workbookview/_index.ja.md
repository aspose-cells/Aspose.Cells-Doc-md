---
title: ## Node.jsとC++を利用したブックビューの制御方法
linktitle: ワークブックビューの制御方法
type: docs
weight: 600
url: /ja/nodejs-cpp/how-to-control-workbook-view/
description: Aspose.Cells for Node.js via C++ APIを使用してブックビューを制御する方法を学びます。
keywords: ワークブックビューをC++経由のNode.jsで制御する方法、ExcelビューをC++経由のNode.jsで設定する方法、C++経由のNode.jsでワークブックビューを操作する方法、C++経由のNode.jsでワークブックビューを設定する方法、C++経由のNode.jsでExcelビューを制御する方法。
---

## **可能な使用シナリオ**
Excelページの表示を調整する必要がある場合、横スクロールバーや縦スクロールバーの制御、開いたExcelファイルを非表示にするかどうかなど、各モジュールの制御方法を知る必要があります。Aspose.Cells for Node.js via C++はこの機能を提供します。Aspose.Cells for Node.js via C++は、あなたの目標達成を助けるための以下のプロパティとメソッドを提供します。

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.getWindowHeight()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowHeight--)
- [**WorkbookSettings.getWindowWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowWidth--)
- [**WorkbookSettings.getWindowLeft()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowLeft--)
- [**WorkbookSettings.getWindowTop()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowTop--)

## **Aspose.Cells for Node.js via C++を使用してワークブックビューを制御する方法**
この例では、次のことができます:

1. ワークブックを作成する。
1. 最初のワークシートのセルにデータを追加する。
1. ワークブックビューの水平および垂直のスクロールバーを非表示にする。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating an Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

cell = cells.get("E10");
const temp = workbook.createStyle();
temp.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(temp);

// Hide horizontal and vertical scrollbars
workbook.getSettings().setIsHScrollBarVisible(false);
workbook.getSettings().setIsVScrollBarVisible(false);

workbook.save("out.xlsx");
```

結果ファイルのプレビュー:
<br>
<image src="result.png" width="70%" />


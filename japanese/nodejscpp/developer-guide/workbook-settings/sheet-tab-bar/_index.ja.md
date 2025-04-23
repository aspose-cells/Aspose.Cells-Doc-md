---  
title: ## Node.jsとC++を使用したシートタブバーの制御方法  
linktitle: シートタブバーの制御方法  
type: docs  
weight: 600  
url: /ja/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Aspose.Cells for Node.js via C++を使用してシートタブバーを制御する方法を学びます。  
keywords: Node.jsとC++を使用したシートタブバーの制御方法、操作、設定。  
---  

## **可能な使用シナリオ**  
Excelのシートバーの表示を調整する必要がある場合、シートタブバーの非表示や表示、幅の変更、最初に表示されるタブの設定などを制御する方法を知る必要があります。Aspose.Cells for Node.js via C++はこれらの機能をサポートしています。Aspose.Cellsは、これらの設定を実現するためのプロパティとメソッドを提供します。

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Aspose.Cells for Node.js via C++を使用したシートタブバーの制御方法**  
この例では、次のことができます:

1. ワークブックを作成する。
1. 最初のワークシートのセルにデータを追加する。
1. シートタブを表示してタブバーの幅を設定します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
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

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

結果ファイルのプレビュー:  
<br>  
<image src="result.png" width="70%" />  



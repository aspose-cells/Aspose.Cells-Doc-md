---
title: Node.js経由のC++を使用してMicrosoft ExcelのFormula Watch Windowにセルを追加
linktitle: Microsoft Excelフォーミュラ監視ウィンドウにセルを追加する
description: Aspose.Cellsライブラリを使用して、Node.js経由のC++でExcelの式ウォッチウィンドウにセルを追加する方法の概要。既存のExcelファイルをロードするか新規作成し、そのセルを操作し、式を設定します。最後に変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、Formula Watch Window、セルの追加、Node.js via C++
type: docs
weight: 60
url: /ja/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能な使用シナリオ**

Microsoft Excelのウォッチウィンドウは、セルの値とその式を便利に監視できるツールです。Excelで*Watch Window*を開くには、*数式 > 監視 > ウィンドウ*をクリックします。*Add Watch*ボタンでセルを検査のために追加できます。同様に、[**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-)メソッドを使用してAspose.Cells APIでセルを*ウォッチウィンドウ*に追加できます。

## **Microsoft Excelフォーミュラ計算エンジンのAspose.Cells**

以下のサンプルコードは、セルC1とE1の式を設定し、それらをウォッチウィンドウに追加しています。その後、ワークブックを[出力Excelファイル](67338481.xlsx)として保存します。出力Excelファイルを開き、*ウォッチウィンドウ*を確認すると、両方のセルがこのスクリーンショットのように表示されます。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}

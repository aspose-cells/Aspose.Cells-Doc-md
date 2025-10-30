---
title: Node.js経由でC++を使ったドロップダウンリストによるダイナミックチャートの作成方法
linktitle: ドロップダウンリストを使用した動的チャートの作成方法
description: Aspose.Cells for Node.js via C++を使用して、ドロップダウンリスト選択に基づいて更新されるダイナミックチャートの作成方法を学びます。ステップバイステップのガイドでは、チャートにドロップダウンリストを統合し、柔軟なデータ視覚化を実現する方法を示します。
keywords: Aspose.Cells for Node.js via C++、ダイナミックチャート、ドロップダウンリスト、データビジュアリゼーション、統合、柔軟な可視化。
type: docs
weight: 76
url: /ja/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **可能な使用シナリオ**
Excelでのドロップダウンリストを使用した動的チャートは、選択したデータに基づいてダイナミックに更新されるインタラクティブなチャートをユーザーが作成できる強力なツールです。この機能は、複数のデータセットを分析したり、さまざまなシナリオを比較したりする必要がある状況で特に有用です。

ドロップダウンリストを使用した動的チャートの一般的な応用例は、財務分析です。たとえば、企業には異なる年や部門の複数の財務データがあるかもしれません。ドロップダウンリストを使用することで、ユーザーは分析したい特定のデータセットを選択し、チャートは自動的に対応する情報を表示します。これにより、簡単に比較し、トレンドやパターンを特定できます。

もう1つの応用例は、営業とマーケティングです。企業には異なる製品や地域の販売データがあるかもしれません。ドロップダウンリストを使用した動的チャートでは、ユーザーはドロップダウンリストから特定の製品や地域を選択し、チャートは選択したオプションの販売実績を動的に表示します。これにより、トップのパフォーマンスエリアや製品を特定し、データに基づいた意思決定が行えます。

要するに、Excelでのドロップダウンリストを使用した動的チャートは、データを柔軟にインタラクティブに可視化および分析する手段を提供します。複数のデータセットを比較したり、さまざまなシナリオを探ったりする必要がある状況で価値があり、財務分析、営業とマーケティングなど様々な応用に使える多目的なツールです。

## **Aspose Cellsを使用して動的チャートをドロップダウンリストで作成する**
次の段落では、Aspose.Cells for Node.js via C++を使用してドロップダウンリストを持つダイナミックチャートの作成方法を示します。例のコードと、このコードで作成されたExcelファイルも紹介します。

## **サンプルコード**
次のサンプルコードでは、[ドロップダウンリストファイル](DynamicChartWithDropdownlist.xlsx)を生成します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **メモ**
生成されたファイルでは、チャートは選択した月のデータを動的にカウントします。これはサンプルコードでの「OFFSET」式の使用によって行われます。

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

セル「Sheet1!$A$10」のドロップダウンリストの値を変更してみると、チャートが動的に変化することがわかります。これで、Aspose.Cellsを使用して動的なチャートをドロップダウンリストで作成しました。
{{< app/cells/assistant language="nodejs-cpp" >}}

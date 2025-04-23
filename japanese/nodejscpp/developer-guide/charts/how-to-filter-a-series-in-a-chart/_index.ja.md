---
title: Node.js経由でC++を使ったチャートデータのフィルタリングに関する3つの方法
linktitle: チャートデータのフィルタリングの3つの方法
description: Aspose.Cells for Node.js via C++を使用してExcelのチャートをフィルタリングする方法を学びましょう。包括的なガイドでは、チャートにフィルターを適用し、チャート要素をカスタマイズし、データ分析ツールを利用してより良い洞察と情報に基づく意思決定を行う方法を示します。
keywords: Aspose.Cells for Node.js via C++、Excelでのチャートフィルタリング、データ分析、意思決定、可視化。
type: docs
weight: 2210
url: /ja/nodejs-cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. チャートからシリーズをフィルタリングする**

### **Excelでチャートからシリーズをフィルタリングする手順**
Excelでは、特定の系列をフィルタリングして、その系列をチャートに表示しないようにすることができます。元のチャートは**図1**に示されています。ただし、**Testseries2**と**Testseries4**をフィルターアウトすると、チャートは**図2**のように表示されます。

Aspose.Cells for Node.js via C++では、同様の操作を行うことができます。<br>サンプルファイル（[seriesFiltered.xlsx](seriesFiltered.xlsx)）のように、**Testseries2**と**Testseries4**を除外するには、次のコードを実行します。また、選択したすべてのシリーズを格納するリスト（[Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--））も維持します。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](seriesFiltered.xlsx)を読み込みます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. データをフィルターし、グラフを変更します**

データをフィルタリングすると、多くのデータを扱うグラフのフィルター操作が便利になります。データをフィルターすると、グラフも変わります。ただし、フィルター後はグラフが画面から消えないようにする必要があります。フィルターを適用すると、隠された行ができ、その状態ではグラフも隠された行に配置されることがあります。

![todo:image_alt_text](Figure3.png)

### **Excelでチャートを変更するデータフィルターの使用手順**

1. データ範囲の内側をクリックします。
2. **データ** タブをクリックし、フィルターを選択してフィルターをオンにします。 ヘッダー行にはドロップダウン矢印が表示されます。
3. **挿入** タブに移動し、列のチャートを選択して、チャートを作成します。
4. 今、データをドロップダウン矢印を使用してフィルタリングします。 チャートフィルターは使用しないでください。

### **サンプルコード**
次のサンプルコードは、Aspose.Cellsを使用した同じ機能を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. テーブルを使用してデータをフィルターし、グラフを変更します**

テーブルを使用することは、範囲を使用する方法2と似ていますが、テーブルには範囲よりも優れた点があります。 テーブルに範囲を変更してデータを追加すると、チャートが自動的に更新されます。 範囲の場合、データソースを変更する必要があります。

### **Excelでテーブルとしてフォーマット**

データ内をクリックし、**CTRL + T** を使用するか、**ホーム** タブ、**テーブルの書式設定** を使用します。

![todo:image_alt_text](Figure4.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](TableFilters.xlsx)を読み込み、Aspose.Cellsを使用した同じ機能を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```

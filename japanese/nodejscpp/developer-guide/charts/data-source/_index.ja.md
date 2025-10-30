---  
title: Node.jsとC++を使用してチャートのデータソースを設定します  
description: Aspose.Cells for Node.js via C++がサポートするさまざまなデータソースについて学びましょう。ガイドでは利用可能なデータソースの種類と、それらに接続してデータを取得し、ワークシートを埋める方法を案内します。  
keywords: Aspose.Cells for Node.js via C++、チャート作成、データフォーマット、ラベル、色、フォント、外観、使いやすさ。  
linktitle: データソース  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/data-formatting-in-charts/  
---  

以前のトピックで、多くの例を示してチャートのデータソースの設定方法を説明しました。このトピックでは、チャートに設定できるデータの種類について詳細を提供します。

## **チャートデータの設定**

Aspose.Cellsを使用してチャートを作成する際に扱うデータには、次の2種類があります：

- チャートデータ。
- カテゴリデータ。

### **チャートデータ**

チャートのデータは、チャートを構築するために使用するデータソースのデータです。セルの範囲（チャートデータを含む）を [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) オブジェクトの [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-) メソッドを呼び出して追加できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **カテゴリデータ**

カテゴリデータは、チャートデータのラベル付けに使用され、[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) の [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--) プロパティを使用して追加できます。以下に例を示し、チャートとカテゴリデータの使用例を示します。上記の例コードを実行すると、列チャートがワークシートに追加されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **高度なトピック**  
- [行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する](/cells/ja/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [動的なチャートを作成する](/cells/ja/nodejs-cpp/create-dynamic-charts/)  
- [Chart.SetChartDataRangeメソッドを使用した簡単なチャート設定方法](/cells/ja/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [チャートシリーズのX値とY値のタイプを検索する](/cells/ja/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
{{< app/cells/assistant language="nodejs-cpp" >}}

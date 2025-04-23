---
title: Node.jsとC++を使用したチャートの作成と管理
linktitle: チャート
description: Aspose.Cells for Node.jsを使ってMicrosoft Excelでチャートを作成する方法を学びます。さまざまなチャートタイプとその外観や書式設定のカスタマイズ方法を示すガイドです。
keywords: Aspose.Cells for Node.js、チャート作成、Microsoft Excel、チャートタイプ、カスタマイズ、外観、書式設定
type: docs
weight: 130
url: /ja/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

Aspose.Cellsでさまざまなチャートをスプレッドシートに追加できます。Aspose.Cellsは多くの柔軟なチャートオブジェクトを提供します。このトピックでは、Aspose.Cellsのチャートオブジェクトについて説明します。

{{% /alert %}}

## **チャートの作成**

### **単純なチャートの作成**
Aspose.Cellsで次の例コードを使用して簡単にチャートを作成できます：
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **チャート作成のための注意事項**

チャートを作成する前に、Aspose.Cellsを使ってチャートを作成する際に役立つ基本的な概念を理解しておくことが重要です。

#### **チャートオブジェクト**

以下にチャートオブジェクトを一覧します：

- シリーズ、チャート内の単一のデータシリーズ。
- 軸、チャートの軸。
- Chart, 単一のExcelグラフ。
- ChartArea, ワークシート内のグラフエリア。
- ChartDataTable, グラフデータテーブル。
- ChartFrame, グラフ内のフレームオブジェクト。
- ChartPoint, グラフ内のシリーズの単一のポイント。
- ChartPointCollection, 1つのシリーズ内のすべてのポイントを含むコレクション。
- Charts, Chartオブジェクトのコレクション。
- DataLabels, 指定されたシリーズのすべてのDataLabelオブジェクトのコレクション。
- FillFormat, シェイプの塗りつぶし形式。
- Floor, 3Dグラフの床。
- Legend, グラフの凡例。
- Line, グラフの線。
- SeriesCollection, Seriesオブジェクトのコレクション。
- TickLabels, グラフ軸の目盛りのラベル。
- Title, グラフまたは軸のタイトル。
- Trendline, グラフ内のトレンドライン。
- TrendlineCollection, 指定されたデータシリーズのすべてのTrendlineオブジェクトのコレクション。
- Walls, 3Dグラフの壁。

#### **Chartingオブジェクトの使用**

上記のように、すべてのチャートオブジェクトはそれぞれのクラスのインスタンスであり、特定のタスクを実行するための特定のプロパティとメソッドを提供します。チャートオブジェクトを使用して、チャートを作成します。

[**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--)コレクションを使用してワークシートに任意のタイプのチャートを追加します。[**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--)コレクション内の各アイテムは[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)オブジェクトを表します。[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)オブジェクトは、チャートの外観をカスタマイズするために必要なすべての他のチャートオブジェクトをカプセル化しています。次のセクションでは、基本的なチャートオブジェクトを使用してシンプルなチャートを作成する方法を示します。

### **Aspose.Cellsを使用したチャートの作成**

**手順:**

1. [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/)オブジェクトの[**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-)メソッドを使用して、ワークシートのセルにデータを追加します。
   これはグラフのデータソースとして使用されます。
1. [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)コレクションの[**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-)メソッドを呼び出し、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/)オブジェクト内にラップされたチャートをワークシートに追加します。
1. [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)列挙値を使ってチャートのタイプを指定します。
   例えば、以下の例では[**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype)値をチャートタイプとして使用しています。
1. [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)コレクションからインデックスを渡して新しい[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)オブジェクトにアクセスします。
1. [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)オブジェクトにカプセル化されたチャートオブジェクトのいずれかを使用してチャートを管理します。
   以下の例では、[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/)チャートオブジェクトを使用してチャートのデータソースを指定します。

チャートにソースデータを追加する際、データソースはセル範囲（例：「A1:C3」）や連続しないセルのシーケンス（例：「A1, A3, A5」）、値のシーケンス（例：「1,2,3」）のいずれかです。

これらの一般的な手順を使用すると、任意のタイプのチャートを作成できます。異なるチャートオブジェクトを使用して、異なるチャートを作成します。

Aspose.Cellsでさまざまな種類のチャートを作成することが可能です。Aspose.Cellsでサポートされているすべての標準チャートは、[**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)という名前の列挙型で事前定義されています。

事前定義されたチャートの種類は:

|**チャートの種類**|**説明**|
| :- | :- |
|Column| クラスタ化された列チャートを表します。
|ColumnStacked| 積み上げ列チャートを表します。
|Column100PercentStacked| 100% 積み上げ列チャートを表します。
|Column3DClustered| 3D クラスタ化された列チャートを表します。
|Column3DStacked| 3D 積み上げ列チャートを表します。
|Column3D100PercentStacked| 3D 100% 積み上げ列チャートを表します。
|Column3D| 3D 列チャートを表します。
|Bar| クラスタ化された棒チャートを表します。
|BarStacked| 積み上げ棒チャートを表します。
|Bar100PercentStacked| 100% 積み上げ棒チャートを表します。
|Bar3DClustered| 3D クラスタ化された棒チャートを表します。
|Bar3DStacked| 3D 積み上げ棒チャートを表します。
|Bar3D100PercentStacked| 3D 100% 積み上げ棒チャートを表します。
|Line| 折れ線チャートを表します。
|LineStacked| 積み上げ折れ線チャートを表します。
|Line100PercentStacked| 100% 積み上げ折れ線チャートを表します。
|LineWithDataMarkers| データマーカー付きの折れ線チャートを表します。
|LineStackedWithDataMarkers| データマーカー付きの積み上げ折れ線チャートを表します。
|Line100PercentStackedWithDataMarkers| データマーカー付きの100% 積み上げ折れ線チャートを表します。
|Line3D| 3D 折れ線チャートを表します。
|Pie| 円グラフを表します。
|Pie3D| 3D 円グラフを表します。
|PiePie| パイ オブ パイ チャートを表します。
|PieExploded| 分解された円グラフを表します。
|Pie3DExploded| 3Dエクスプロード円グラフを表します|
|PieBar| パイチャートのバーを表します|
|Scatter| 散布図を表します|
|ScatterConnectedByCurvesWithDataMarker| データマーカー付きの曲線で接続された散布図を表します|
|ScatterConnectedByCurvesWithoutDataMarker| データマーカーなしの曲線で接続された散布図を表します|
|ScatterConnectedByLinesWithDataMarker| データマーカー付きの線で接続された散布図を表します|
|ScatterConnectedByLinesWithoutDataMarker| データマーカーなしの線で接続された散布図を表します|
|Area| エリアチャートを表します|
|AreaStacked| 積み上げエリアチャートを表します|
|Area100PercentStacked| 100% 積み上げエリアチャートを表します|
|Area3D| 3Dエリアチャートを表します|
|Area3DStacked| 3D積み上げエリアチャートを表します|
|Area3D100PercentStacked| 3D 100% 積み上げエリアチャートを表します|
|Doughnut| ドーナツチャートを表します|
|DoughnutExploded| 分裂したドーナツチャートを表します|
|Radar| レーダーチャートを表します|
|RadarWithDataMarkers| データマーカー付きのレーダーチャートを表します|
|RadarFilled| 塗りつぶしのレーダーチャートを表します|
|Surface3D| 3Dサーフェスチャートを表します|
|SurfaceWireframe3D| ワイヤーフレーム3Dサーフェスチャートを表します|
|SurfaceContour| 等高線チャートを表します|
|SurfaceContourWireframe| ワイヤーフレーム等高線チャートを表します|
|Bubble| バブルチャートを表します|
|Bubble3D| 3Dバブルチャートを表します|
|Cylinder| シリンダーチャートを表します|
|CylinderStacked| 積み上げシリンダーチャートを表します|
|Cylinder100PercentStacked| 100% 積み上げシリンダーチャートを表します|
|CylindericalBar| 円柱形バーチャートを表します|
|CylindericalBarStacked| 積み上げ円柱形バーチャートを表します|
|CylindericalBar100PercentStacked| 100% 積み上げ円柱形バーチャートを表します|
|CylindericalColumn3D| 3D円柱チャートを表します
|Cone| 円錐チャートを表します
|ConeStacked| 積み重ね円錐チャートを表します
|Cone100PercentStacked| 100% 積み重ね円錐チャートを表します
|ConicalBar| 円錐バーチャートを表します
|ConicalBarStacked 積み重ね円錐バーチャートを表します
|ConicalBar100PercentStacked| 100% 積み重ね円錐バーチャートを表します
|ConicalColumn3D| 3D円錐柱チャートを表します
|Pyramid| ピラミッドチャートを表します
|PyramidStacked| 積み重ねピラミッドチャートを表します
|Pyramid100PercentStacked| 100% 積み重ねピラミッドチャートを表します
|PyramidBar| ピラミッドバーチャートを表します
|PyramidBarStacked| 積み重ねピラミッドバーチャートを表します
|PyramidBar100PercentStacked| 100% 積み重ねピラミッドバーチャートを表します
|PyramidColumn3D| 3Dピラミッド柱チャートを表します
{{% alert color="primary" %}}

セルの範囲をデータソースとして割り当てると、左上から右下までの範囲を設定できます。例えば、"A1:C3"は有効ですが、"C3:A1"は無効です。

{{% /alert %}}

#### **ピラミッドチャート**

例のコードを実行すると、ワークシートにピラミッドチャートが追加されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **折れ線グラフ**

上記の例では、[**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)を*Line*に変更するだけでラインチャートが作成されます。完全なソースは以下に示します。コードを実行すると、ワークシートにラインチャートが追加されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **バブルチャート**

バブルチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)を[**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype)に設定し、BubbleSizes、Values、XValuesなどいくつかの追加プロパティを適切に設定する必要があります。次のコードを実行すると、ワークシートにバブルチャートが追加されます。

#### **データマーカー付きラインチャート**

データマーカー付きラインチャートを作成するには、[**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)を*ChartType.LineWithDataMarkers*に設定し、背景エリア、Series Markers、Values、XValuesなどいくつかの追加プロパティを適切に設定する必要があります。以下のコードを実行すると、データマーカー付きのラインチャートがワークシートに追加されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **高度なトピック**
- [Excel 2016のチャートの読み込みと操作](/cells/ja/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Excelチャートの軸の管理](/cells/ja/nodejs-cpp/chart-axes/)
- [グラフの外観設定](/cells/ja/nodejs-cpp/setting-chart-appearance/)
- [チャートタイプ](/cells/ja/nodejs-cpp/chart-types/)
- [チャートのカスタマイズ](/cells/ja/nodejs-cpp/customizing-charts/)
- [チャートのデータソースを設定する](/cells/ja/nodejs-cpp/data-formatting-in-charts/)
- [Excelチャートのデータラベルの管理](/cells/ja/nodejs-cpp/insert-datalabels-to-chart/)
- [チャートのワークシートを取得する](/cells/ja/nodejs-cpp/get-worksheet-of-the-chart/)
- [Excelチャートの凡例の管理](/cells/ja/nodejs-cpp/chart-legend/)
- [チャートの位置、サイズ、デザインの操作](/cells/ja/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [リーダーライン付き円グラフの作成](/cells/ja/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [グラフ内の図形](/cells/ja/nodejs-cpp/controls-in-charts/)
- [Excelグラフのタイトルの管理](/cells/ja/nodejs-cpp/chart-and-axis-titles/)
- [グラフのレンダリング](/cells/ja/nodejs-cpp/chart-rendering/)
- [グラフトレンドラインの方程式テキストを取得](/cells/ja/nodejs-cpp/get-equation-text-of-chart-trendline/)

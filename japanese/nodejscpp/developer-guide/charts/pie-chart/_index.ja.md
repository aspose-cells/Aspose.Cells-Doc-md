---
title: Node.js経由でLeader Lines付きの円グラフを作成する方法
description: Microsoft ExcelでLeader Lines付きの円グラフを作成するためにAspose.Cells for Node.js via C++を使用する方法を学びましょう。ガイドでは、データポイントと凡例を接続するリーダーラインの追加手順と、チャートの全体的な見やすさ向上について解説します。
keywords: Aspose.Cells for Node.js via C++、円グラフ、リーダーライン、Microsoft Excel、データ可視化、チャートカスタマイズ。
linktitle: 円グラフ
type: docs
weight: 45
url: /ja/nodejs-cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

この記事では、Aspose.Cells for Node.js via C++ APIを使用してリーダーライン付きの円グラフを一から作成する方法を説明します。Excelでは、「リーダーラインを表示」オプションがデフォルトで設定されており、円グラフを作成するとリーダーラインが表示されます。ただし、Aspose.Cells APIを使用して同様のグラフを作成する場合は、明示的に [**Series.getHasLeaderLines()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getHasLeaderLines--) プロパティを設定する必要があります。

{{% /alert %}}

リーダーライン付き円グラフを作成するためにAspose.Cells for Node.js via C++ APIの使用例を示すために、新しい [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) を作成し、系列のデータソースとなるデータを入力します。データの準備ができたら、[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) の [**ChartType.Pie**](https://reference.aspose.com/cells/nodejs-cpp/charttype) 型のチャートをコレクションに追加し、そのさまざまな側面を設定して、目的のビューを実現します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);
```

これまでに円グラフを作成し、異なる側面を設定しました。これからは、チャートのリーダーラインをオンにします。リーダーラインを表示するには、データラベルを少し移動する必要があります。

次のコードは、リーダーラインをオンにし、チャートを更新し、それからデータラベルの位置を計算して適切に移動します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);

// Turn on leader lines
chart.getNSeries().get(0).setHasLeaderLines(true);

// Calculate chart
chart.calculate();

// You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
const DELTA = 100;
for (let i = 0; i < chart.getNSeries().get(0).getPoints().getCount(); i++) {
let X = chart.getNSeries().get(0).getPoints().get(i).getDataLabels().getX();
// If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
if (X > 2000)
chart.getNSeries().get(0).getPoints().get(i).getDataLabels().setX(X + DELTA);
else
chart.getNSeries().get(0).getPoints().get(i).getDataLabels().setX(X - DELTA);
}
```

最後に、次のコードでチャートを画像形式で保存し、ワークブックをXLSX形式で保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook in XLSX format
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add two columns of data
worksheet.getCells().get("A1").putValue("Retail");
worksheet.getCells().get("A2").putValue("Services");
worksheet.getCells().get("A3").putValue("Info & Communication");
worksheet.getCells().get("A4").putValue("Transport Equip");
worksheet.getCells().get("A5").putValue("Construction");
worksheet.getCells().get("A6").putValue("Other Products");
worksheet.getCells().get("A7").putValue("Wholesale");
worksheet.getCells().get("A8").putValue("Land Transport");
worksheet.getCells().get("A9").putValue("Air Transport");
worksheet.getCells().get("A10").putValue("Electric Appliances");
worksheet.getCells().get("A11").putValue("Securities");
worksheet.getCells().get("A12").putValue("Textiles & Apparel");
worksheet.getCells().get("A13").putValue("Machinery");
worksheet.getCells().get("A14").putValue("Metal Products");
worksheet.getCells().get("A15").putValue("Cash");
worksheet.getCells().get("A16").putValue("Banks");

worksheet.getCells().get("B1").putValue(10.4);
worksheet.getCells().get("B2").putValue(5.2);
worksheet.getCells().get("B3").putValue(6.4);
worksheet.getCells().get("B4").putValue(10.4);
worksheet.getCells().get("B5").putValue(7.9);
worksheet.getCells().get("B6").putValue(4.1);
worksheet.getCells().get("B7").putValue(3.5);
worksheet.getCells().get("B8").putValue(5.7);
worksheet.getCells().get("B9").putValue(3);
worksheet.getCells().get("B10").putValue(14.7);
worksheet.getCells().get("B11").putValue(3.6);
worksheet.getCells().get("B12").putValue(2.8);
worksheet.getCells().get("B13").putValue(7.8);
worksheet.getCells().get("B14").putValue(2.4);
worksheet.getCells().get("B15").putValue(1.8);
worksheet.getCells().get("B16").putValue(10.1);

// Create a pie chart and add it to the collection of charts
const id = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

// Access newly created Chart instance
const chart = worksheet.getCharts().get(id);

// Set series data range
chart.getNSeries().add("B1:B16", true);

// Set category data range
chart.getNSeries().setCategoryData("A1:A16");

// Turn off legend
chart.setShowLegend(false);

// Access data labels
const dataLabels = chart.getNSeries().get(0).getDataLabels();

// Turn on category names
dataLabels.setShowCategoryName(true);

// Turn on percentage format
dataLabels.setShowPercentage(true);

// Set position
dataLabels.setPosition(AsposeCells.LabelPositionType.OutsideEnd);

// Set separator
dataLabels.setSeparatorType(AsposeCells.DataLabelsSeparatorType.Comma);

// In order to save the chart image, create an instance of ImageOrPrintOptions
const anOption = new AsposeCells.ImageOrPrintOptions();

// Set image format
anOption.setImageType(AsposeCells.ImageType.Png);

// Set resolution
anOption.setHorizontalResolution(200);
anOption.setVerticalResolution(200);

// Render chart to image
chart.toImage(path.join(dataDir, "output_out.png"), anOption);

// Save the workbook to see chart inside the Excel
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

|**作成された円グラフ**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高度なトピック**
- [円グラフでのカスタムスライスまたはセクターの色](/cells/ja/nodejs-cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける](/cells/ja/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 関連記事

- [チャートの作成](/cells/ja/nodejs-cpp/creating-charts/)
- [チャートのカスタマイズ](/cells/ja/nodejs-cpp/customizing-charts/)
- [グラフのデータ整形](/cells/ja/nodejs-cpp/data-formatting-in-charts/)
- [グラフの外観設定](/cells/ja/nodejs-cpp/setting-chart-appearance/)

{{< app/cells/assistant language="nodejs-cpp" >}}

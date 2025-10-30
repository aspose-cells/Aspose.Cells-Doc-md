---
title: Node.jsをC++経由でトルネードチャートを作成する方法
linktitle: 竜巻チャートの作成方法
type: docs
weight: 73
url: /ja/nodejs-cpp/create-tornado-chart/
description: Aspose.Cells for Node.js via C++ APIを使ってトルネードチャートを作成する方法を学びましょう。
keywords: Node.jsでトルネードチャートを作成し、トルネードチャートを追加し、挿入する方法
---

## **紹介**
竜巻チャート、または竜巻ダイアグラムまたは竜巻グラフとしても知られるものは、Excelで感度分析によく使用されるデータの視覚化タイプです。これは、特定の結果や成果に対する変数変更の影響を理解するのに役立ちます。

## **Excelで竜巻チャートを作成する方法**
Excelで竜巻チャートを作成する方法は次の通りです：
1. データを選択し、挿入 --> グラフ --> 挿入列または棒グラフ --> 積み上げ棒グラフに移動し、そこをクリックします。
<br>
<img src="1.png" width=70% />
2. Y軸を変更：Y軸を右クリックします。軸の書式設定をクリックします。ラベルで、ラベル位置ドロップダウンをクリックして、Low項目を選択します。
<br>
<img src="2.png" width=70% />
3. 任意の棒を選択し、書式設定に移動します。適切なギャップ幅を設定します。
<br>
<img src="3.png" width=70% />
4. 竜巻チャートからマイナス記号（-）を削除しましょう。X軸を選択します。書式設定に移動し、軸オプションで数字をクリックします。カテゴリでカスタムを選択し、フォーマットコードに###0,###0を記入します。追加をクリックします。
<br>
<img src="4.png" width=70% />
5. Y軸をクリックし、軸オプションに移動します。軸オプションで逆順でカテゴリをチェックします。
<br>
<img src="5.png" width=70% />

## **Aspose.Cells for Node.js via C++でトルネードチャートを追加する方法**
次のサンプルコードをご覧ください。[サンプルExcelファイル](sample.xlsx)を読み込み、いくつかのサンプルデータが含まれているとします。次に、初期データに基づいて積み上げ棒グラフを作成し、関連するプロパティを設定します。最後に、ワークブックを[出力XLSX形式](out.xlsx)に保存します。次のスクリーンショットは、出力ExcelファイルでAspose.Cellsによって作成された竜巻チャートを示しています。
<br>
<img src="6.png" width=70% />

### **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);
const charts = sheet.getCharts();
// Add bar chart
const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
const chart = charts.get(index);

// Set data for bar chart
chart.setChartDataRange("A1:C7", true);

// Set properties for bar chart
chart.getTitle().setText("Tornado chart");
chart.setStyle(2);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getPlotArea().getBorder().setColor(AsposeCells.Color.White);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

chart.getCategoryAxis().setTickLabelPosition(AsposeCells.TickLabelPositionType.Low);
chart.getCategoryAxis().setIsPlotOrderReversed(true);

chart.setGapWidth(10);

const valueAxis = chart.getValueAxis();
valueAxis.getTickLabels().setNumberFormat("#,##0;#,##0");

workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}

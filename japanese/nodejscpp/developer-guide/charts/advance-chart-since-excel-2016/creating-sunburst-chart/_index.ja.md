---
title: Node.jsとC++を使用したサンバーストチャートの作成方法
linktitle: サンバーストチャートの作成方法
description: Aspose.Cells for Node.js via C++で放射状チャートを作成する方法について学習します。このチャートはデータを円形で表示します。ガイドでは、チャートのさまざまなプロパティと書式設定（データラベル、凡例、色など）の設定方法を解説します。
keywords: Aspose.Cells for Node.js via C++、サンバーストチャート、作成、設定、データラベル、凡例、フォーマット、色、円、データレンダリング。
type: docs
weight: 162
url: /ja/nodejs-cpp/creating-sunburst-chart/
---

## **可能な使用シナリオ**
ツリーマップチャートは階層内の比率を比較するのに適していますが、最大カテゴリと各データポイント間の階層レベルを表示するには最適ではありません。サンバーストチャートはそれを表示するのに非常に適したビジュアルです。サンバーストチャートは階層データの表示に理想的です。各階層は一つのリングまたは円で表され、最も内側の円が階層のトップです。階層データのないサンバーストチャート（カテゴリ一つのレベル）はドーナツチャートと似ています。ただし、複数レベルのカテゴリを持つサンバーストチャートは外側のリングが内側のリングとどのように関連しているかを示します。サンバーストチャートは、一つのリングがどのようにその寄与部分に分解されるかを示すのに最も効果的であり、もう一つの階層チャートであるツリーマップは相対的なサイズの比較に最適です。

![todo:image_alt_text](sample.png)
## **サンバーストチャート**
以下のコードを実行すると、下記のサンバーストチャートが表示されます。

![todo:image_alt_text](result.png)
## **サンプルコード**
下記のサンプルコードは、[サンプルExcelファイル](sunburst.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}

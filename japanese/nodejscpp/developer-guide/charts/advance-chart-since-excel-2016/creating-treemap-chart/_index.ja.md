---  
title: Node.jsとC++を使用したツリーマップチャートの作成方法  
linktitle: ツリーマップチャートの作成方法  
description: Aspose.Cells for Node.js via C++を使用してTreemapチャートを作成する方法について学びます。ガイドでは、ツリーマップチャートのさまざまなプロパティとフォーマットオプション（色、ラベル、データ表現など）を理解するのに役立ちます。  
keywords: Aspose.Cells for Node.js、ツリーマップチャート、作成、プロパティ、フォーマット、色、ラベル、データ表現、円形チャート、階層チャート。  
type: docs  
weight: 161  
url: /ja/nodejs-cpp/creating-treemap-chart/  
---  

## **可能な使用シナリオ**  
ツリーマップチャートは、データを階層ビューで表し、店舗の売れ筋商品などのパターンを簡単に把握できます。ツリーのブランチは長方形で表され、各サブブランチは小さな長方形として表示されます。ツリーマップチャートは、色と近接性でカテゴリを表示し、他のチャートタイプでは難しい大量のデータを簡単に表示できます。  

![todo:image_alt_text](sample.png)  
## **ツリーマップチャート**  
以下のコードを実行すると、下記のツリーマップチャートが表示されます。  

![todo:image_alt_text](result.png)  
## **サンプルコード**  
下記のサンプルコードは、[サンプルExcelファイル](treemap.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

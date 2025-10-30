---  
title: Node.jsを使ったC++によるExcelチャートの軸管理  
description: Aspose.Cells for Node.js via C++でチャートの軸を設定する方法を学びます。ガイドでは、プライマリおよびセカンダリ軸の調整、範囲設定、プロパティの変更方法を紹介し、チャートの見栄えを向上させる方法を説明します。  
keywords: Aspose.Cells for Node.js via C++、チャート軸、設定、プライマリ軸、セカンダリ軸、範囲、プロパティ。  
linktitle: 軸  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

Excelチャートには、3種類の軸があります。  
1. 水平（カテゴリ）軸：X軸  
1. 垂直（値）軸：Y軸  
1. 深度（シリーズ）軸：Z軸  

{{% /alert %}}  

## **軸オプション**  
Aspose.Cells for Node.js via C++では、実行時にチャートの軸を管理することも可能です。 [Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/) オブジェクトを使うと、Excelと同様にすべての軸のオプションを変更できます。  

|![todo:image_alt_text](chart_axes.png)|  

## **X軸とY軸を管理する**  
Excelのチャートでは、水平方向と垂直方向の軸が最も一般的に使用される軸です。  

次のコードスニペットは、X軸とY軸のオプション設定方法を示しています。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **高度なトピック**  
- [目盛りラベル方向の変更](/cells/ja/nodejs-cpp/change-tick-label-direction/)  
- [チャートに存在する軸を特定する](/cells/ja/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Microsoft Excelのようにチャートの軸の自動単位を処理する](/cells/ja/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [チャートを計算した後に軸ラベルを読み取る](/cells/ja/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Excelチャートでカテゴリ軸を設定する方法](/cells/ja/nodejs-cpp/how-to-set-category-axis/)  

{{< app/cells/assistant language="nodejs-cpp" >}}

---  
title: Node.jsを使用してC++経由でチャート系列内のポイントのX値とY値のタイプを見つける方法  
linktitle: チャートシリーズのポイントのXおよびY値のタイプを検索する  
description: Aspose.Cells for Node.js via C++を使って、チャート系列のポイントのX値とY値のタイプを判定する方法を学びましょう。このガイドでは、データ値の種類と、それをチャートでアクセスして操作する方法について説明しています。  
keywords: Aspose.Cells for Node.js、チャート作成、X値、Y値、データタイプ、アクセス、操作、チャート系列。  
type: docs  
weight: 150  
url: /ja/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **可能な使用シナリオ**  
 時々、系列内のチャートポイントのX値とY値のタイプを知りたい場合があります。Aspose.Cells for Node.js via C++では、`ChartPoint.XValueType`と`ChartPoint.YValueType`プロパティがこれに使用できます。ただし、これらのプロパティを効果的に使用する前に`Chart.calculate()`メソッドを呼び出す必要があります。  

## **チャートシリーズのX値とY値のタイプを検索する**  
 以下のサンプルコードは、[サンプルExcelファイル](64716905.xlsx)を読み込み、最初のワークシート内の最初のチャートにアクセスします。次に、`Chart.calculate()`メソッドを呼び出し、最初のチャートポイントのX値とY値のタイプを調べ、コンソールに出力します。参考のために下記のコンソール出力を参照してください。  

## **サンプルコード**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Load sample Excel file containing chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart.
const chart = worksheet.getCharts().get(0);

// Calculate chart data.
chart.calculate();

// Access first chart point in the first series.
const point = chart.getNSeries().get(0).getPoints().get(0);

// Print the types of X and Y values of chart point.
console.log("X Value Type: " + point.getXValueType());
console.log("Y Value Type: " + point.getYValueType());
```  

## **コンソール出力**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}

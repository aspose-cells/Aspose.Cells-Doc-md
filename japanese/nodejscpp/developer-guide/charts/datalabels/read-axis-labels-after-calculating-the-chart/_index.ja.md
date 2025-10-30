---  
title: チャートの軸ラベルを計算後に読む方法：Node.js経由のC++  
linktitle: チャートの計算後に軸ラベルを読む  
description: Aspose.Cells for Node.js via C++でチャートを計算した後、軸ラベルを読む方法を学びましょう。ガイドでは、軸ラベルへのアクセス方法、取得方法、その書式設定や位置について説明します。  
keywords: Aspose.Cells for Node.js、チャート、軸ラベル、計算、読み取り、アクセス、取得、書式設定、位置、Node.js経由のC++  
type: docs  
weight: 90  
url: /ja/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **可能な使用シナリオ**

 チャートの値を計算した後、軸ラベルを読み取るには[**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--)メソッドを使用します。この目的のために、[**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--)メソッドを利用してください。これにより軸ラベルのリストが返されます。

## **チャートを計算した後に軸ラベルを読み取る**

次のサンプルコードは、[サンプルExcelファイル](ReadAxisLabels.xlsx)を読み込み、最初のワークシートのチャートのカテゴリ軸ラベルを読み取ります。その後、軸ラベルの値をコンソールに出力します。参考のために、以下に示すサンプルコードのコンソール出力をご覧ください。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **コンソール出力**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}

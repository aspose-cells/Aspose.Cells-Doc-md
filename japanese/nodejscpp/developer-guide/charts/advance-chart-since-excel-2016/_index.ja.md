---  
title: Node.js を介して Excel 2016 のチャートを読み取り、操作する方法  
linktitle: Excel 2016のチャートの読み込みと操作  
description: Aspose.Cells for Node.js via C++ を使用して Excel 2016 のチャートを読み取り、操作する方法を学びます。このガイドでは、さまざまなチャートのプロパティにアクセスおよび変更する方法を示します。  
keywords: Aspose.Cells for Node.js、Excel 2016 チャート、読み取り、操作、データラベル、シリーズ色、レイアウト、階層チャート、円形チャート。  
type: docs  
weight: 48  
url: /ja/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **可能な使用シナリオ**  
Aspose.Cellsは、Microsoft Excel 2016のチャートの読み取りと操作をサポートしています。これらは、Microsoft Excel 2013以前のバージョンには存在しません。  
## **Excel 2016のチャートの読み込みと操作**  
次のサンプルコードは、Excel 2016のチャートを含む最初のワークシートがある[ソースExcelファイル](22774101.xlsx)を読み込みます。すべてのチャートを一つ一つ読み取り、そのチャートの種類に応じてタイトルを変更します。以下のスクリーンショットは、コード実行前のソースExcelファイルを示しています。ご覧の通り、すべてのチャートのタイトルは同じです。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

次のスクリーンショットは、コードを実行した後の[出力エクセルファイル](22774104.xlsx)を示しています。ご覧のとおり、チャートのタイトルがチャートタイプに応じて変更されています。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **サンプルコード**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **コンソール出力**  
提供された[ソースエクセルファイル](22774101.xlsx)で上記のサンプルコードを実行した際のコンソール出力は次のとおりです。

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **高度なトピック**  
- [ウォーターフォールチャートの作成](/cells/ja/nodejs-cpp/creating-waterfall-chart/)  
- [ツリーマップチャートの作成](/cells/ja/nodejs-cpp/creating-treemap-chart/)  
- [サンバーストチャートの作成](/cells/ja/nodejs-cpp/creating-sunburst-chart/)  


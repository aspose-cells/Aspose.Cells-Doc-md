---  
title: ChartGlobalizationSettingsクラスを使ってNode.jsとC++でチャートコンポーネントの異なる言語を設定  
linktitle: ChartGlobalizationSettingsクラスを使用して、チャートコンポーネントの異なる言語を設定する方法  
description: Aspose.Cells for Node.js via C++でChartGlobalizationSettingsクラスを使用し、チャートのコンポーネントに異なる言語を設定する方法を学びます。ガイドでは、チャート要素、ラベル、凡例のローカライズ方法を解説します。  
keywords: Aspose.Cells for Node.js via C++、チャート作成、チャートのグローバリゼーション、言語、ローカライズ、ChartGlobalizationSettings、要素、ラベル、凡例。  
type: docs  
weight: 2200  
url: /ja/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **可能な使用シナリオ**  

Aspose.Cells APIは[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)クラスを公開しており、これはユーザーがスプレッドシート内のチャートコンポーネントを異なる言語に設定し、小計のカスタムラベルも作成できるようにするためです。  

## **ChartGlobalizationSettingsクラスの紹介**  

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)クラスは、現在8つのメソッドを提供しており、これらをカスタムクラスでオーバーライドして、軸タイトル名、軸単位名、チャートタイトル名などを異なる言語に翻訳できます。  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--)：軸タイトルの名前を取得します。  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-)：軸単位の名前を取得します。  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--)：チャートタイトルの名前を取得します。  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--)：凡例の減少の名前を取得します。  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--)：凡例の増加を示す名前を取得。  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--)：凡例の合計の名前を取得します。  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--)：チャートの「その他」ラベルの名前を取得します。  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--)：チャート内の系列の名前を取得します。  

### **カスタム言語の翻訳**  
以下、次のデータを元にウォーターフォールチャートを作成します。チャートコンポーネントの名前は、チャート内で英語で表示されます。チャートタイトル、凡例の増減名、合計名、および軸タイトルのトルコ語表示方法を示すためにトルコ語の例を使用します。  

![todo:image_alt_text](sample.png)  

## **サンプルコード**  
次のサンプルコードは、[サンプルExcelファイル](waterfall.xlsx)を読み込みます。  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
getChartTitleName() {
return "Grafik Başlığı"; // Chart Title
}
getLegendIncreaseName() {
return "Artış"; // Increase
}
getLegendDecreaseName() {
return "Düşüş"; // Decrease
}
getLegendTotalName() {
return "Toplam"; // Total
}
getAxisTitleName() {
return "Eksen Başlığı"; // Axis Title
}
}

async function chartGlobalizationSettingsTest() {
// Create an instance of existing Workbook
const dataDir = path.join(__dirname, "data");
const pathName = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(pathName);

// Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
workbook.getSettings().getGlobalizationSettings().setChartSettings(new TurkeyChartGlobalizationSettings());

// Get the worksheet 
const worksheet = workbook.getWorksheets().get(0);
const chartCollection = worksheet.getCharts();

// Load the chart from source worksheet
const chart = chartCollection.get(0);

// Chart Calculate
chart.calculate();

// Get the chart title
const title = chart.getTitle();
console.log("\nWorkbook chart title: " + title.getText());

const legendEntriesLabels = chart.getLegend().getLegendLabels();

// Output the name of the Legend 
legendEntriesLabels.forEach(label => {
console.log("\nWorkbook chart legend: " + label);
```  

## サンプルコードによって生成された出力  

これは上記のサンプルコードのコンソール出力です。  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}

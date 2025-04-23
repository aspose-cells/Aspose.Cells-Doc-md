---  
title: Excelチャートを画像に変換する Node.js via C++  
linktitle: Excel チャートを画像に変換する  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/convert-an-excel-chart-to-image/  
description: Excelチャートを画像に変換する方法をAspose.Cells for Node.js via C++を使って学びます。  
---  

{{% alert color="primary" %}}  

チャートは視覚的に魅力的であり、データの比較、パターン、トレンドをユーザーに見やすく表示するのに役立ちます。例えば、ワークシートの数列を分析するよりも、チャートを見ると一目で売上が減少しているか増加しているか、実際の売上が予測された売上と比較してどうなっているかが分かります。人々は統計情報や図情報をわかりやすく、かつ簡単に維持できるように提示するように頻繁に求められます。図が手助けします。  

時々、アプリケーションやWebページにはチャートが必要になる場合があります。あるいは、Word文書、PDFファイル、PowerPointプレゼンテーション、または他のアプリケーションで必要となることもあります。どの場合でも、チャートを画像としてレンダリングし、他の場所で使用できるようにしたいです。  

{{% /alert %}}  

## **チャートをイメージに変換する**  

ここでは、円グラフと棒グラフを画像に変換しています。  

### **円グラフを画像ファイルに変換する**  

最初にMicrosoft Excelで円グラフを作成し、次にAspose.Cells for Node.js via C++を使って画像ファイルに変換します。この例のコードは、テンプレートMicrosoft Excelファイル内の円グラフに基づいてEMF画像を作成します。  

|**出力: 円グラフ画像**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Microsoft Excelで円グラフを作成:  
   1. Microsoft Excelで新しいブックを開きます。  
   1. ワークシートにデータを入力します。  
   1. データに基づいて円グラフを作成します。  
   1. ファイルを保存します。  

|**入力ファイル**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Aspose.Cellsをダウンロードしてインストールします。  
   1. [Aspose.Cells for Node.js via C++をダウンロード](https://downloads.aspose.com/cells/nodejs-cpp)。  
   1. 開発コンピュータにインストールします。  

全ての[Aspose](http://www.aspose.com/)コンポーネントは、最初にインストールした際に評価モードで動作します。評価モードには時間制限はなく、出力ドキュメントに透かしを挿入するだけです。  

1. プロジェクトを作成します。  
   1. 好きなIDEを起動します。  
   1. 新しいコンソールアプリケーションを作成します。この例はNode.jsアプリケーションを使用していますが、任意のJavaScriptランタイム環境で作成できます。  
   1. 参照を追加します。このプロジェクトはAspose.Cellsを使用しているため、Aspose.Cells for Node.js via C++への参照を追加してください。  
   1. チャートを見つけて変換するコードを記述します。以下にコンポーネントがこのタスクを遂行するために使用するコードが示されています。ごく少数の行のコードが使用されます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

### **棒グラフを画像ファイルに変換する**  

まず、Microsoft Excelで縦棒グラフを作成し、それを画像ファイルに変換します。サンプルコードを実行した後、テンプレートExcelファイルの縦棒グラフに基づいてJPEGファイルが作成されます。  

|**出力ファイル: 棒グラフ画像**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Microsoft Excelで棒グラフを作成します:  
   1. Microsoft Excelで新しいブックを開きます。  
   1. ワークシートにデータを入力します。  
   1. データに基づいて棒グラフを作成します。  
   1. ファイルを保存します。  

|**入力ファイル**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. 上記のように説明した参照を含むプロジェクトを設定します。  
1. チャートを動的に画像に変換します。以下にコンポーネントがこのタスクを遂行するために使用するコードが示されています。このコードは前述のものと似ています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  


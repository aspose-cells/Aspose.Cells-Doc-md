---
title: C++経由のJavaScriptでExcelチャートを画像に変換
linktitle: Excel チャートを画像に変換する
type: docs
weight: 20
url: /ja/javascript-cpp/convert-an-excel-chart-to-image/
description: C++経由のAspose.Cells for JavaScriptを使用してExcelチャートを画像に変換する方法を学びます。
---

{{% alert color="primary" %}}  

チャートは視覚的に魅力的であり、データの比較、パターン、トレンドをユーザーに見やすく表示するのに役立ちます。例えば、ワークシートの数列を分析するよりも、チャートを見ると一目で売上が減少しているか増加しているか、実際の売上が予測された売上と比較してどうなっているかが分かります。人々は統計情報や図情報をわかりやすく、かつ簡単に維持できるように提示するように頻繁に求められます。図が手助けします。  

時々、アプリケーションやWebページにはチャートが必要になる場合があります。あるいは、Word文書、PDFファイル、PowerPointプレゼンテーション、または他のアプリケーションで必要となることもあります。どの場合でも、チャートを画像としてレンダリングし、他の場所で使用できるようにしたいです。  

{{% /alert %}}  

## **チャートをイメージに変換する**  

ここでは、円グラフと棒グラフを画像に変換しています。  

### **円グラフを画像ファイルに変換する**  

まず、Microsoft Excelで円グラフを作成し、その後、C++経由のAspose.Cells for JavaScriptを使用して画像ファイルに変換します。この例のコードは、テンプレートMicrosoft Excelファイルに基づいてEMF画像を作成します。  

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
   1. [C++経由のAspose.Cells for JavaScriptをダウンロード](https://downloads.aspose.com/cells/javascript-cpp)。  
   1. 開発コンピュータにインストールします。  

全ての[Aspose](http://www.aspose.com/)コンポーネントは、最初にインストールした際に評価モードで動作します。評価モードには時間制限はなく、出力ドキュメントに透かしを挿入するだけです。  

1. プロジェクトを作成します。  
   1. 好きなIDEを起動します。  
   1. 新しいコンソールアプリケーションを作成します。この例ではJavaScriptアプリケーションを使用していますが、任意のJavaScript実行環境を使用して作成できます。  
   1. 参照を追加します。このプロジェクトではAspose.Cellsを使用しているため、C++経由のAspose.Cells for JavaScriptへの参照を追加してください。  
   1. チャートを見つけて変換するコードを記述します。以下にコンポーネントがこのタスクを遂行するために使用するコードが示されています。ごく少数の行のコードが使用されます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
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

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```

---
title: JavaScriptを使用してワークシートを拡大縮小する方法
linktitle: ワークシートを縮尺する方法
type: docs
weight: 130
url: /ja/javascript-cpp/how-to-scale-a-worksheet/
description: この記事は、C++を使ったAspose.Cells for JavaScriptを使用してワークシートを拡大縮小する方法を説明するコード例を示します。
keywords: JavaScriptでワークシートを拡大縮小する方法、C++を用いたJavaScriptでのワークシートの拡大縮小、JavaScriptを使ったワークシートの拡大縮小
---

## **可能な使用シナリオ**
ワークシートの縮尺は、作業するコンテキストによってさまざまな理由で便利です。一般的な理由をいくつか挙げます：
1. ページに収める：印刷時にすべての内容が1ページまたは指定したページ数に収まるようにし、読みやすさと管理の容易さを確保します。

1. プレゼンテーション：シートをより整理されたプロフェッショナルな外観にし、会議やレポートで他者と共有しやすくします。

1. 可読性：文字や他の要素のサイズを調整して、特に小さなフォントの読みづらさを感じる人々にとっても読みやすくします。

1. スペース管理：シート上のスペースの最適化を図り、不必要な空白を避け、重要な情報が過剰なスクロールなしで見えるようにします。

1. データビジュアル化：チャートやグラフの場合、適切なスペースに収めるためにサイズを調整し、見やすさを向上させることができます。

1. 一貫性：複数のシートやドキュメント間で見た目の一貫性を保つために、特にプロフェッショナルや教育環境で重要です。

## **Excelでワークシートを縮尺する方法**
Excelでシートをスケールすることで、印刷時にコンテンツを単一ページや指定したページ数に収めることができます。手順は次のとおりです：

1. シートを開く：スケールしたいExcelシートを開きます。

1. ページレイアウトタブへ移動：「リボン」内の「ページレイアウト」タブをクリックします。

1. スケール調整グループ：「ページレイアウト」タブ内の「スケール調整」グループを見つけます。ここでスケーリングの調整が行えます。幅：印刷されるシートの横幅ページ数を指定します。高さ：縦方向のページ数を指定します。スケール：カスタムの割合を設定することも可能です。
<br>
<img src="1.png" width=60% />

1. 幅と高さの設定：希望のページ数に設定します。例えば、シートを1ページに収めたい場合は両方とも1に設定します。

1. スケーリング割合の調整（必要に応じて）：特定の割合に設定したい場合は、Scaleボックスを調整します。例えば50%に設定すると、すべてが半分の大きさになります。


## **JavaScriptを使用してC++経由でワークシートを拡大縮小する方法**
C++を介したAspose.Cells for JavaScriptは、Excelファイルをプログラム的に操作するための強力なライブラリです。Aspose.Cellsを使用してワークシートを拡大縮小するには、次の手順に従います：サンプルファイル（sample.xlsx）を読み込み、印刷設定を調整して内容が希望のページ数または元のサイズの特定の割合に収まるようにします。

### **例：ページに収める**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **例：パーセンテージにスケール**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />

---
title: Microsoft Excelのように自動単位を処理するために、JavaScriptを使用してC++でチャート軸の自動単位を管理します
linktitle: Microsoft Excelのようにチャートの軸の自動単位を処理する
description: C++を使ったAspose.Cells for JavaScriptでチャート軸の自動単位の処理方法を学びましょう。自動単位の設定やカスタマイズ、科学的表記の表示、スケールの調整方法を紹介します。
keywords: C++を使用したAspose.Cells for JavaScript、チャート軸、自動単位、Microsoft Excel、設定、カスタマイズ、科学的表記、スケーリング
type: docs
weight: 120
url: /ja/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **可能な使用シナリオ**  
以前のC++を使用したAspose.Cells for JavaScriptのバージョンでは、チャートを画像やPDFにレンダリングする際に軸の自動単位を適切に処理できませんでした。現在では、C++を使用したAspose.Cells for JavaScriptは軸の自動単位の処理をサポートしています。コードの変更は必要なく、チャートを画像やPDFに変換するだけで、Microsoft Excelのように軸がレンダリングされます。  

## **Microsoft Excelのようにチャートの軸の自動単位を処理する**  
次のサンプルコードは、[サンプルExcelファイル](61767755.xlsx)を読み込み、[出力PDFチャート](61767752.pdf)を生成します。スクリーンショットは、チャート軸の自動単位を赤い長方形で示し、サンプルExcelファイルのチャートと出力されたPDFのチャートを比較しています。両者は完全に一致しています。  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **サンプルコード**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

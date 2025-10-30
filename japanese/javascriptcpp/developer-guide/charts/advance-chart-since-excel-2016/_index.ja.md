---
title: JavaScriptを通じてC++でExcel 2016のチャートを読み取り、操作する
linktitle: Excel 2016のチャートの読み込みと操作
description: C++を通じてAspose.Cells for JavaScriptでExcel 2016のチャートを読み取り、操作する方法について学びます。このガイドは、さまざまなチャートのプロパティにアクセスし、変更する方法を示します。
keywords: C++を通じてAspose.Cells for JavaScriptでExcel 2016のチャート、読み取り、操作、データラベル、シリーズの色、レイアウト、階層型チャート、円形チャート。
type: docs
weight: 48
url: /ja/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **可能な使用シナリオ**  
Aspose.Cellsは、Microsoft Excel 2016のチャートの読み取りと操作をサポートしています。これらは、Microsoft Excel 2013以前のバージョンには存在しません。  
## **Excel 2016のチャートの読み込みと操作**  
次のサンプルコードは、Excel 2016のチャートを含む最初のワークシートがある[ソースExcelファイル](22774101.xlsx)を読み込みます。すべてのチャートを一つ一つ読み取り、そのチャートの種類に応じてタイトルを変更します。以下のスクリーンショットは、コード実行前のソースExcelファイルを示しています。ご覧の通り、すべてのチャートのタイトルは同じです。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

次のスクリーンショットは、コードを実行した後の[出力エクセルファイル](22774104.xlsx)を示しています。ご覧のとおり、チャートのタイトルがチャートタイプに応じて変更されています。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **サンプルコード**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **コンソール出力**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **高度なトピック**  
- [ウォーターフォールチャートの作成](/cells/ja/javascript-cpp/creating-waterfall-chart/)  
- [ツリーマップチャートの作成](/cells/ja/javascript-cpp/creating-treemap-chart/)  
- [サンバーストチャートの作成](/cells/ja/javascript-cpp/creating-sunburst-chart/)

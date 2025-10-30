---
title: JavaScriptを使用してC++経由でチャートのデータラベル形状をテキストに合わせてリサイズする方法
linktitle: チャートのデータラベルの形状をテキストに合わせるようにサイズ変更する
description: Aspose.Cells for JavaScript via C++を使用してチャートのデータラベルの形状をテキストにフィットさせてリサイズする方法を学びましょう。ガイドでは、ラベルのサイズと形状を調整し、テキストが正しく表示され重なりや途中で切れるのを防ぎます。
keywords: Aspose.Cells for JavaScript via C++、チャート作成、データラベル、形状リサイズ、テキストフィット、切り詰め、重なり。
type: docs
weight: 220
url: /ja/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
Excelアプリケーションでは、チャートのデータラベルの**テキストに合わせて形状を変更**するオプションが提供されており、これによりテキストが形状内に収まるように形状のサイズが拡大されます。  
{{% /alert %}}  

## **Microsoft Excelのインタフェース上で、チャートのデータラベルを選択して、**フォーマットデータラベル**メニューを右クリックします。**サイズとプロパティ**タブで、**配置**を展開して、**テキストに合わせて形状を変更**オプションを含む関連プロパティを表示します。**  

 このオプションは、チャート上の任意のデータラベルを選択し、右クリックして**データラベルの書式設定**メニューからアクセスできます。**サイズとプロパティ**タブの下にある**整列**を展開すると、必要な関連プロパティが表示されます、その中に**テキストに合わせて形状をリサイズ**オプションがあります。  

## **Aspose.Cells for JavaScript via C++を使用してチャートのデータラベルの形状をテキストに合わせてリサイズする方法**  

 Excelの機能に似せて、データラベルの形状をテキストにフィットさせるために、Aspose.Cells APIはブール型の[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--)プロパティを公開しています。以下のコード例は、その[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--)プロパティの簡単な使用例を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

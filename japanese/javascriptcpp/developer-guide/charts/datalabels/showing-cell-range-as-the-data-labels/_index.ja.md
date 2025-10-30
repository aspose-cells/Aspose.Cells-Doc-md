---
title: JavaScriptを使ったチャートのセル範囲データラベル表示（C++経由）
linktitle: データラベルとしてのセル範囲を表示
description: Aspose.Cells for JavaScriptを使ってチャートにセル範囲をデータラベルとして表示する方法を学びます。このガイドでは、ラベルをデータソースにリンクし、正確で意味のある情報を提供するためのフォーマット方法を解説します。
keywords: Aspose.Cells for JavaScriptを使ったC++によるチャートのセル範囲データラベル表示、データソースのフォーマット、正確さ、意味のある情報。
type: docs
weight: 130
url: /ja/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
Microsoft Excel 2013では、データラベルにセル範囲を表示できます。Aspose.Cells for JavaScriptはこの機能をサポートしています。
{{% /alert %}}

## **セル範囲をデータラベルとして表示するためのチェックボックス**

Microsoft Excelでセルの範囲をデータラベルとして表示するには：

1. シリーズのデータラベルを選択して、コンテキストメニューを開くために右クリックします。  
1. **データラベルの書式設定**を選択します。ラベルのオプションが表示されます。  
1. **ラベルに値を含める**オプションを選択またはクリアします。  

以下のサンプルコードは、チャートシリーズのデータラベルにアクセスし、その[**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--)プロパティを**true**に設定して、「セル値からのラベル」オプションを選択します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
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

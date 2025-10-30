---
title: JavaScriptを使ってC++経由でチャートのワークシートを取得する方法
linktitle: チャートのワークシートを取得
description: Aspose.Cells for JavaScriptを使ってExcelチャートに関連付けられたワークシートを取得する方法を学び、効率的にチャートの基礎データにアクセス・操作します。
keywords: Aspose.Cells for JavaScript、Excelチャート、ワークシート、データ操作、基礎データ、操作、JavaScript経由のC++
type: docs
weight: 1000
url: /ja/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

時には、チャートの参照からワークシートにアクセスしたい場合があります。Aspose.Cellsは、チャートを含むワークシートの参照を返す[**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)プロパティを提供しています。

{{% /alert %}}

以下の例は [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) プロパティの使用例を示します。最初にワークシートの名前を出力し、その後最初のチャートにアクセスします。再びワークシート名を出力し、[**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) プロパティを使用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

以下はサンプルコードのコンソール出力です。同じワークシート名が2回印刷されることがわかります。

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}

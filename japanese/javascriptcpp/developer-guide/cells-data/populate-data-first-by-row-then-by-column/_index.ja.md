---
title: 最初に行、次に列ごとにデータを埋めます
type: docs
weight: 1000
url: /ja/javascript-cpp/populate-data-first-by-row-then-by-column/
description: まず行単位でデータを入力し、その後列単位でデータを入力する方法をAspose.Cells for JavaScriptはC++ APIを通じて学びます。
keywords: 行単位でデータを入力、次に列単位でデータを入力 JavaScript経由C++、 行単位でデータ挿入、次に列単位でJavaScript経由C++、 最初にデータを追加、次に列単位でJavaScript経由C++、 高性能なデータ挿入JavaScript経由C++、 高性能なデータ追加JavaScript経由C++
---

{{% alert color="primary" %}}  

スプレッドシートにデータを最初に行ごと、次に列ごとに埋めると、全体のパフォーマンスが向上します。  

{{% /alert %}}  

A1、B1、A2、B2の順にデータを入れることは、A1、A2、B1、B2の順よりも速くなります。ワークシートに多くのセルがある場合、データを行ごとに入力する場合、このヒントはプログラムをはるかに高速化できます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

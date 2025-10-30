---
title: チャートの凡例エントリーの塗りつぶしをなしに設定するには、Aspose.Cells for JavaScriptを用いたC++を利用します。
linktitle: Aspose.Cellsを使用して、チャートの凡例エントリの塗りつぶしのテキストを無効に設定する
description: C++経由でAspose.Cells for JavaScriptを使用して、グラフの凡例エントリの塗りつぶしをなしに設定する方法を学びます。このガイドでは、Microsoft Excelのチャートで凡例エントリの塗りつぶし色を変更し、視覚化とカスタマイズを向上させる方法を示します。
keywords: Aspose.Cells for JavaScriptをC++経由で使用, チャート凡例エントリの塗りつぶし, Microsoft Excel, 視覚化, カスタマイズ。
type: docs
weight: 320
url: /ja/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

チャートの凡例エントリの塗りつぶしを「なし」に設定して、凡例内に表示されないようにする場合は、[**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--)を**true**に設定してください。

{{% /alert %}}

次のサンプルコードは、チャートの2番目の凡例エントリの塗りつぶしのテキストを無効に設定します。このコードで使用される [サンプルExcelファイル](5115219.xlsx) とその生成される [出力Excelファイル](5115217.xlsx) をダウンロードして参照してください。

次のスクリーンショットは、このコードが[sample excel file](5115219.xlsx)に与える影響を示しています。

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

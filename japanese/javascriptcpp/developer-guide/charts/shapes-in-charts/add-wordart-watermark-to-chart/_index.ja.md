---
title: ChartにWordArtウォーターマークを追加するJavaScriptをC++経由で使用
linktitle: グラフにWordArtウォーターマークを追加する
description: C++を使ってMicrosoft ExcelのチャートにWordArtウォーターマークを追加する方法を学びます。ガイドでは、WordArtウォーターマークを作成し、配置して、チャートの視覚的魅力と独自性を向上させる方法を示します。
keywords: Aspose.Cells for JavaScript、WordArtウォーターマーク、チャートウォーターマーク、Microsoft Excel、視覚的魅力、チャートの独自性。
type: docs
weight: 50
url: /ja/javascript-cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}}  

WordArtを使用して、スプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルを伸ばしたり、テキストを飾ったり、テキストをプリセットされた形に合わせたり、チャートのプロットエリアに影響を及ぼすテキストを透かしとして適用したりできます。WordArtは移動したり配置したりしてスプレッドシートに装飾を追加できるオブジェクトになります。  

次の例は、グラフのプロットエリアにウォーターマークとしてWordArtシェイプを追加する方法を示しています。  

{{% /alert %}}  

次の例では、既存のチャートのプロットエリアにWordArt形状をウォーターマークとして追加する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add WordArt Watermark to Chart</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet's first chart
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Add a WordArt watermark (shape) to the chart's plot area
            const wordart = chart.shapes.addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
                "CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

            // Get the shape's fill format and set transparency
            const wordArtFormat = wordart.fill;
            wordArtFormat.transparency = 0.9;

            // Get the line format and set weight to invisible (0.0)
            const lineFormat = wordart.line;
            lineFormat.weight = 0.0;

            // Save the modified workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">WordArt watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

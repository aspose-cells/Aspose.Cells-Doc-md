---
title: C++を使用したSunburstチャートの作成方法
linktitle: サンバーストチャートの作成方法
description: C++を経由してAspose.Cells for JavaScriptで円形のデータ表示を行うサンバーストチャートの作成方法を学習しましょう。ガイドはデータラベル、凡例、色などのさまざまなプロパティや書式設定の設定をサポートします。
keywords: C++を使用したAspose.Cells for JavaScriptのサンバーストチャート作成、プロパティ設定、データラベル、凡例、フォーマット、色、円形、データレンダリング。
type: docs
weight: 162
url: /ja/javascript-cpp/creating-sunburst-chart/
---

## **可能な使用シナリオ**
ツリーマップチャートは階層内の比率を比較するのに適していますが、最大カテゴリと各データポイント間の階層レベルを表示するには最適ではありません。サンバーストチャートはそれを表示するのに非常に適したビジュアルです。サンバーストチャートは階層データの表示に理想的です。各階層は一つのリングまたは円で表され、最も内側の円が階層のトップです。階層データのないサンバーストチャート（カテゴリ一つのレベル）はドーナツチャートと似ています。ただし、複数レベルのカテゴリを持つサンバーストチャートは外側のリングが内側のリングとどのように関連しているかを示します。サンバーストチャートは、一つのリングがどのようにその寄与部分に分解されるかを示すのに最も効果的であり、もう一つの階層チャートであるツリーマップは相対的なサイズの比較に最適です。

![todo:image_alt_text](sample.png)
## **サンバーストチャート**
以下のコードを実行すると、下記のサンバーストチャートが表示されます。

![todo:image_alt_text](result.png)
## **サンプルコード**
下記のサンプルコードは、[サンプルExcelファイル](sunburst.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

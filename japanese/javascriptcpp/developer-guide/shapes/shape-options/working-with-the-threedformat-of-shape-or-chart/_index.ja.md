---
title: JavaScriptを使用してC++経由でShapeまたはChartのThreeDFormatを操作する方法
linktitle: 図形またはグラフの3 D形式の操作
type: docs
weight: 250
url: /ja/javascript-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **可能な使用シナリオ**
Aspose.Cells for JavaScript via C++は、[Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--)プロパティと[ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat)クラスを提供し、ShapeやChartの3Dフォーマットを操作します。[ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat)クラスには、アプリケーションの要件に応じて異なる結果を得るために設定できるさまざまなプロパティがあります。

## **図形またはグラフの3-D形式の操作**
次のサンプルコードは、[ソースExcelファイル](5115419.xlsx)を読み込み、最初のシートの最初の図形にアクセスし、[Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--)プロパティのサブプロパティを設定してから、ワークブックを[出力Excelファイル](5115410.xlsx)に保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Apply 3D Format Example</title>
    </head>
    <body>
        <h1>Apply 3D Format to Shape</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const ws = workbook.worksheets.get(0);

            const sh = ws.shapes.get(0);

            const n3df = sh.threeDFormat;
            n3df.contourWidth = 17;
            n3df.extrusionHeight = 32;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">3D formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

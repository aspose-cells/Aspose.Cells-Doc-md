---
title: JavaScript経由でC++を使用してワークシート間でシェイプ（図やチャートなど）をコピーする
linktitle: シェイプをコピーする
type: docs
weight: 200
url: /ja/javascript-cpp/copy-shapes-between-worksheets/
description: Aspose.Cells for JavaScriptを使用してワークシート間で画像やチャートなどのシェイプをコピーする方法を学びます。
---

{{% alert color="primary" %}}

場合によっては、ワークシート間で画像やチャートなどの要素をコピーする必要があります。Aspose.Cells for JavaScriptはこの機能をサポートしています。チャートや画像、その他のオブジェクトは最高精度でコピー可能です。

この記事では、ワークシート間でシェイプをコピーする方法について詳しく説明します。

{{% /alert %}}

## **ワークシート間での画像のコピー**

ワークシート間での画像のコピーには、以下のサンプルコードに示すように [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) メソッドを使用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Picture Between Worksheets</h1>
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

            // Get the Picture from the "Picture" worksheet.
            const pictureSheet = workbook.worksheets.get("Picture");
            const pictureSource = pictureSheet.pictures.get(0);

            // Save Picture to Memory (property access converted from getData())
            const ms = pictureSource.data;

            // Copy the picture to the Result Worksheet (properties converted)
            const resultSheet = workbook.worksheets.get("Result");
            resultSheet.pictures.add(
                pictureSource.upperLeftRow,
                pictureSource.upperLeftColumn,
                ms,
                pictureSource.widthScale,
                pictureSource.heightScale
            );

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PictureCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **ワークシート間でのグラフのコピー**

次のコードは、[**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addCopy-shape-number-number-number-number-) メソッドを使用して、ワークシート間でのチャートのコピーを示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Chart Between Sheets Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Chart from the "Chart" worksheet.
            const chartsource = workbook.worksheets.get("Chart").charts.get(0);
            const cshape = chartsource.chartObject;

            // Copy the Chart to the Result Worksheet
            workbook.worksheets.get("Result").shapes.addCopy(cshape, 20, 0, 2, 0);

            // Save the Worksheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **ワークシート間でのコントロールおよびその他の図形オブジェクトのコピー**

コントロールやその他の描画オブジェクトをコピーするには、次の例のように[**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addCopy-shape-number-number-number-number-)メソッドを使用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Shapes Between Worksheets</title>
    </head>
    <body>
        <h1>Copy Shapes Between Worksheets</h1>
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

            // Open the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Shapes from the "Control" worksheet.
            const controlShapes = workbook.worksheets.get("Control").shapes;

            // Copy the Textbox to the Result Worksheet
            workbook.worksheets.get("Result").shapes.addCopy(controlShapes.get(0), 5, 0, 2, 0);

            // Copy the Oval Shape to the Result Worksheet
            workbook.worksheets.get("Result").shapes.addCopy(controlShapes.get(1), 10, 0, 2, 0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ControlsCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

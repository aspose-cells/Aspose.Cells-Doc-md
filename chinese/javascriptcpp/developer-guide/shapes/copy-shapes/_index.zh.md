---
title: 用JavaScript通过C++在工作表之间复制形状
linktitle: 复制形状
type: docs
weight: 200
url: /zh/javascript-cpp/copy-shapes-between-worksheets/
description: 学习如何使用Aspose.Cells for JavaScript通过C++在工作表之间复制图片、图表等形状。
---

{{% alert color="primary" %}}

有时需要在工作表之间复制元素，例如图片、图表和其它绘图对象。Aspose.Cells for JavaScript通过C++支持此功能。图表、图片和其他对象可以以最高精度复制。

本文详细介绍了如何在工作表之间复制形状。

{{% /alert %}}

## **从一个工作表复制图片到另一个工作表**

要将图片从一个工作表复制到另一个，请使用以下示例代码中显示的 [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) 方法。

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

## **将图表从一个工作表复制到另一个**

以下代码演示了使用 [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addCopy-shape-number-number-number-number-) 方法将图表从一个工作表复制到另一个。

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

## **从一个工作表复制控件和其他绘图对象到另一个**

若要复制控件和其他绘图对象，请使用 [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addCopy-shape-number-number-number-number-) 方法，如下面的示例所示。

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

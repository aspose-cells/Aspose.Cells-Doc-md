---
title: 用JavaScript通过C++分屏Excel工作表
linktitle: 分割屏幕
type: docs
weight: 190
url: /zh/javascript-cpp/how-to-split-screen-of-excel-worksheet
description: 在本文中，您将学习如何通过JavaScript结合C++插件以编程方式将工作表分成两个或四个部分，从而显示某些行和/或列。
keywords: 冻结顶部行，冻结顶部行。
---

## **介绍**

在本文中，我们将学习如何通过分屏将工作表分成两部分或四部分，以显示特定的行和/或列。在处理大型数据集时，我们需要同时查看同一工作表中的几个区域以便比较不同的数据子集。分屏功能可以满足您的需求。

## **如何在Excel中分割屏幕**
要将工作表分割成两个或四个部分，请按照以下操作：

1. 选择要分割的行/列/单元格之前的位置。
2. 在“查看”选项卡上，在“窗口”组中，单击“拆分”按钮。

**![拆分屏幕](Split-Screen.png)**

## **在列上垂直拆分工作表**

要在电子表格的两个区域垂直分隔，选择要在其右侧出现分隔的列，并在Excel中单击“拆分”按钮。

通过Aspose.Cells for JavaScript和C++，可以很容易地以编程方式垂直拆分工作表，方法是选择顶行中的一个单元格作为活动单元格，然后使用[**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--)方法拆分。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets C1 cell in the top row as the active cell.
            sheet.activeCell = "C1";

            // Split worksheet vertically on columns
            sheet.split();

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **在行上水平拆分工作表**
要在Excel中水平分隔您的Excel窗口，请选择要在其下方发生分隔的行。

通过Aspose.Cells for JavaScript和C++，可以很容易地以编程方式水平拆分工作表，方法是选择左列中的一个单元格作为活动单元格，然后使用[**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--)方法拆分。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Sets A6 cell in the left column as the active cell.
            sheet.activeCell = "A6";

            // Split worksheet horizontally on rows
            sheet.split();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **将工作表分成四部分**
要同时查看同一工作表的四个不同部分，请在Excel中垂直和水平拆分屏幕。

通过Aspose.Cells for JavaScript和C++，可以很容易地以编程方式垂直拆分工作表，方法是选择不在第一行和第一列中的某个单元格作为活动单元格，然后使用[**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--)方法拆分。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Active Cell and Split Worksheet Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets E6 cell as the active cell.
            sheet.activeCell = "E6";

            // Split worksheet into four parts
            sheet.split();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **如何移除拆分**
要移除工作表的拆分，只需再次单击“拆分”按钮。

Aspose.Cells for JavaScript通过C++提供了一个[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--)方法来移除拆分设置。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Worksheet Example</title>
    </head>
    <body>
        <h1>Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Remove split and then split worksheet into four parts
            sheet.removeSplit();
            sheet.split();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet split operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

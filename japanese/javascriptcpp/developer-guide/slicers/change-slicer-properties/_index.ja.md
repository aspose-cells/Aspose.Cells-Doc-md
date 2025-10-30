---
title: JavaScriptをC++経由で使用してスライサーのプロパティを変更
linktitle: スライサープロパティを変更する
type: docs
weight: 70
url: /ja/javascript-cpp/change-slicer-properties/
---

## **可能な使用シナリオ**

スライサーの配置や行の高さなどのプロパティを変更したい場合があるかもしれません。Aspose.Cells for JavaScriptをC++で使用してこれらのプロパティを更新するオプションを提供します。

## **スライサープロパティを変更する**

次のサンプルコードをご覧ください。最初の列を含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込み、その後、高さ、幅、印刷可能、タイトルなどのプロパティを変更したスライサーを作成します。ワークブックを[outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx)として保存します。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Slicer to Excel Table Example</title>
    </head>
    <body>
        <h1>Create Slicer to Excel Table Example</h1>
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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first table inside the worksheet.
            const table = worksheet.listObjects.get(0);

            // Add slicer
            const idx = worksheet.slicers.add(table, 0, "H5");

            const slicer = worksheet.slicers.get(idx);
            slicer.placement = AsposeCells.PlacementType.FreeFloating;
            slicer.rowHeightPixel = 50;
            slicer.widthPixel = 500;
            slicer.title = "Aspose";
            slicer.alternativeText = "Alternate Text";
            slicer.isPrintable = false;
            slicer.isLocked = false;

            // Refresh the slicer.
            slicer.refresh();

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeSlicerProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Slicer added and properties changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

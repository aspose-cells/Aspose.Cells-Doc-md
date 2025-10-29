---
title: 用JavaScript和C++更改切片器属性
linktitle: 更改切片器属性
type: docs
weight: 70
url: /zh/javascript-cpp/change-slicer-properties/
---

## **可能的使用场景**

在某些情况下，您可能希望更改切片器的位置或行高等属性。Aspose.Cells for JavaScript通过C++为您提供了更新这些属性的选项。

## **更改切片器属性**

请查看以下示例代码。它加载包含表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器，并更改其属性，如行高、宽度、是否可打印、标题等。将工作簿另存为[outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx)。

## **示例代码**

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

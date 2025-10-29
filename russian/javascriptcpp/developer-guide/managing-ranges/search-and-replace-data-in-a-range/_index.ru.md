---
title: Поиск и замена данных в диапазоне с помощью JavaScript через C++
linktitle: Поиск и замена данных в диапазоне
type: docs
weight: 170
url: /ru/javascript-cpp/search-and-replace-data-in-a-range/
description: Эта статья показывает, как искать и заменять данные в диапазоне в Excel, используя JavaScript через C++.
keywords: Поиск и замена данных в Excel с помощью JavaScript, поиск данных в Excel с помощью JavaScript, поиск и замена данных в диапазоне с помощью JavaScript, поиск данных в диапазоне, поиск данных в диапазоне, поиск данных в Excel, поиск данных в диапазоне, поиск данных в диапазоне Excel, поиск данных в диапазоне, поиск и замена данных в Excel с помощью JavaScript, поиск и замена данных в диапазоне с помощью JavaScript, поиск и замена данных в диапазоне с помощью JavaScript
---

{{% alert color="primary" %}}

Иногда необходимо искать и заменять конкретные данные в диапазоне, игнорируя значения ячеек за пределами нужного диапазона. Script через C++ позволяет ограничить поиск определенным диапазоном. В этой статье объясняется, как это сделать.

{{% /alert %}}

Script через C++ предоставляет метод [**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-) для задания диапазона при поиске данных. Ниже приведен пример кода, ищущий и заменяющий данные в диапазоне.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Find and Replace Example</title>
    </head>
    <body>
        <h1>Find and Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FindOptions, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Define the search range (E9:H15)
            const area = CellArea.createCellArea("E9", "H15");

            // Configure find options
            const opts = new FindOptions();
            opts.lookInType = LookInType.Values;
            opts.lookAtType = LookAtType.EntireContent;
            opts.range = area;

            let cell = null;

            do {
                cell = worksheet.cells.find("search", cell, opts);
                if (cell === null || cell.isNull()) {
                    break;
                }
                // Replace found cell's value
                cell.value = "replace";
            } while (true);

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Find and replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

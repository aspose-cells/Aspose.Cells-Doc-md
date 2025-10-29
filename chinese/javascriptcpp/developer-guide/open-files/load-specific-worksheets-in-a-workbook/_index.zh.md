---
title: 用JavaScript通过C++加载工作簿中的特定工作表
linktitle: 加载工作簿中指定的工作表
type: docs
weight: 100
url: /zh/javascript-cpp/load-specific-worksheets-in-a-workbook/
description: 学习如何用Aspose.Cells for JavaScript通过C++加载特定工作表。提高性能，减少内存占用。
---

{{% alert color="primary" %}}

默认情况下，Aspose.Cells会将整个电子表格加载到内存中。也可以只加载特定的工作表。这样可以提高性能，减少内存消耗。在处理由许多工作表组成的大型工作簿时，这种方法非常有用。

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - LoadOptions with Custom Load Filter</title>
    </head>
    <body>
        <h1>Load Workbook with LoadOptions and Custom Load Filter</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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

        // Minimal CustomLoad implementation suitable for assigning as a loadFilter.
        // Adjust methods as needed for your filtering logic.
        class CustomLoad {
            constructor() {
                // Initialize any needed state here
            }

            // Example method name - actual Aspose.Cells LoadFilter interface methods
            // may differ; this placeholder can be extended to meet real interface.
            accept(entry) {
                // Return true to load, false to skip (placeholder logic)
                return true;
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create LoadOptions and assign custom load filter (property assignment)
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);
            loadOptions.loadFilter = new CustomLoad();

            // Create the workbook using the uploaded file and the specified load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Perform your desired task here
            // (left intentionally blank - modify as needed)

            // Save the workbook to a downloadable Blob
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Load Filter Example</title>
    </head>
    <body>
        <h1>Custom Load Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, Utils } = AsposeCells;

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

        class CustomLoad extends AsposeCells.LoadFilter {
            startSheet(sheet) {
                if (sheet.name === "Sheet2") {
                    // Load everything from worksheet "Sheet2"
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All;
                } else {
                    // Load nothing (only structure)
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.Structure;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new CustomLoad();

            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook loaded with custom load filter. Click the download link to save the result.</p>';
        });
    </script>
</html>
```

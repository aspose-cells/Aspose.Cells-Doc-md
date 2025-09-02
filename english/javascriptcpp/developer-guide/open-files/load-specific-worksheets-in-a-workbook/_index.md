---
title: Load Specific Worksheets in a Workbook with JavaScript via C++
linktitle: Load Specific Worksheets in a Workbook
type: docs
weight: 100
url: /javascript-cpp/load-specific-worksheets-in-a-workbook/
description: Learn how to load specific worksheets in a workbook using Aspose.Cells for JavaScript via C++. Improve performance and reduce memory consumption.
---

{{% alert color="primary" %}}

By default, Aspose.Cells loads the whole spreadsheet into memory. It is possible to only load specific sheets. This can improve performance and consume less memory. This approach is useful when working with a large workbook made up of many worksheets.

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
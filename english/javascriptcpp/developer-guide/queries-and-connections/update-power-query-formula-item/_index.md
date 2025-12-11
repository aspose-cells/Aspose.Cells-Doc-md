---
title: Update Power Query Formula Item with JavaScript via C++
linktitle: Update Power Query Formula Item
type: docs
weight: 120
url: /javascript-cpp/update-power-query-formula-item/
description: Learn how to update the Power Query Formula item data source in an Excel file using Aspose.Cells for JavaScript via C++.
---

## **Usage Scenario**

There might be cases where the data source files are moved and the Excel file is unable to locate them. In such cases, Aspose.Cells API provides the option to update the Power Query Formula item by using the [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem) class to update the location of the source file.

## **Updating Power Query Formula Item**

Aspose.Cells API provides the ability to update Power Query Formula Items. The following code snippet demonstrates updating the data source file location in the Excel file by using the [**PowerQueryFormulaItem.value**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem/#value--) property. The source and output files are attached for your reference.

- [Source File 1](106364953.xlsx)
- [Source File 2](106364954.xlsx)
- [Output File](106364955.xlsx)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Power Query Formula Update Example</h1>
        <p>Select the workbook containing Power Query formulas and an optional source workbook to reference in the "Source" item.</p>
        <input type="file" id="fileInputMain" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="fileInputSource">Optional source file (used in the Power Query "Source" item):</label>
        <input type="file" id="fileInputSource" accept=".xls,.xlsx,.csv" />
        <br/><br/>
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
            const result = document.getElementById('result');
            const fileInputMain = document.getElementById('fileInputMain');
            if (!fileInputMain.files.length) {
                result.innerHTML = '<p style="color: red;">Please select the main Excel file containing Power Query formulas.</p>';
                return;
            }

            const fileMain = fileInputMain.files[0];
            const arrayBuffer = await fileMain.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the mashup data and Power Query formulas
            const mashupData = workbook.dataMashup;
            const powerQueryFormulas = mashupData.powerQueryFormulas;
            const count = powerQueryFormulas.count;

            for (let i = 0; i < count; i++) {
                const formula = powerQueryFormulas.get(i);
                const items = formula.powerQueryFormulaItems;
                const itemsCount = items.count;
                for (let j = 0; j < itemsCount; j++) {
                    const item = items.get(j);
                    if (item.name === "Source") {
                        const sourceFileInput = document.getElementById('fileInputSource');
                        const sourceFile = sourceFileInput.files.length ? sourceFileInput.files[0] : null;
                        const sourceName = sourceFile ? sourceFile.name : "SamplePowerQueryFormulaSource.xlsx";
                        // Update the Source item's value to reference the selected source file name
                        item.value = `Excel.Workbook(File.Contents("${sourceName}"), null, true)`;
                    }
                }
            }

            // Saving the modified workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outputFileName = fileMain.name.replace(/\.[^/.]+$/, '') + '_out.xlsx';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outputFileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            result.innerHTML = '<p style="color: green;">Power Query formulas updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
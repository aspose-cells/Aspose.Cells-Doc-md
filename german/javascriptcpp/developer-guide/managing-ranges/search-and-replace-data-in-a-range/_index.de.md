---
title: Daten in einem Bereich mit JavaScript über C++ suchen und ersetzen
linktitle: Daten in einem Bereich suchen und ersetzen
type: docs
weight: 170
url: /de/javascript-cpp/search-and-replace-data-in-a-range/
description: Dieser Artikel zeigt, wie man Daten in einem Bereich in Excel mit JavaScript über C++ sucht und ersetzt.
keywords: JavaScript Daten in Excel suchen und ersetzen, JavaScript Daten in Excel suchen, Daten in einem Bereich mit JavaScript suchen und ersetzen, Daten in einem Bereich mit JavaScript suchen, JavaScript Daten in einem Bereich suchen, JavaScript Daten in einem Bereich durchsuchen, JavaScript Daten in Excel suchen, JavaScript Daten im Bereich suchen, Daten in Excel mit JavaScript suchen und ersetzen, Daten in einem Bereich mit JavaScript suchen und ersetzen, Daten im Bereich mit JavaScript suchen und ersetzen
---

{{% alert color="primary" %}}

Manchmal müssen Sie gezielt nach bestimmten Daten in einem Bereich suchen und diese ersetzen, ohne Werte außerhalb des gewünschten Bereichs zu berücksichtigen. Aspose.Cells for JavaScript über C++ ermöglicht es, eine Suche auf einen bestimmten Bereich zu beschränken. Dieser Artikel erklärt wie.

{{% /alert %}}

Aspose.Cells for JavaScript über C++ bietet die Methode [**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-) zur Angabe eines Bereichs bei der Suche nach Daten. Das folgende Codebeispiel sucht und ersetzt Daten in einem Bereich.

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

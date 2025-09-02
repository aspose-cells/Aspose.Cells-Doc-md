---
title: Support for German Locale in Named Range Formulae with JavaScript via C++
linktitle: Support for German Locale in Named Range Formulae
type: docs
weight: 60
url: /javascript-cpp/support-for-german-locale-in-named-range-formulae/
description: Learn how to support German locale in named range formulae using Aspose.Cells for JavaScript via C++.
---

English formulae are written into named region. This Excel file can be opened in an environment where the system is configured to German Locale, however, the English formula shall be translated to German language. The following example demonstrates this feature; however, it requires Excel to be installed in German language and the system locale shall be set to German as well.  

Sample file for testing this feature can be downloaded from the following link:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Named Range Example</h1>
        <p>Select an existing Excel macro-enabled workbook (.xlsm) to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
                // No file selected - a new empty workbook will be created
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Define named range name and formula
            const name = "HasFormula";
            const value = '=GET.CELL(48, INDIRECT("ZS",FALSE))';

            // Access worksheets collection
            const wsCol = workbook.worksheets;

            // Add named range and set its reference
            const nameIndex = wsCol.names.add(name);
            const namedRange = wsCol.names.get(nameIndex);
            namedRange.refersTo = value;

            // Save the modified workbook as .xlsm and provide download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleOutputNamedRangeTest.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
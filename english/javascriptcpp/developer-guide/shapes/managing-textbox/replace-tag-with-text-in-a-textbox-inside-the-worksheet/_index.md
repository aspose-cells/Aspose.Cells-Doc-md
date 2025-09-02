---
title: Replace tag with text in a textbox inside the Worksheet with JavaScript via C++
linktitle: Replace tag with text in a textbox inside the Worksheet
type: docs
weight: 1100
url: /javascript-cpp/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Learn how to replace tags with text in a textbox within a worksheet using Aspose.Cells for JavaScript via C++. 
---

## **Possible Usage Scenarios**
Text boxes can have tags which can be replaced with some text at runtime to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Sample Code**
Following sample code replaces tags TAG_1 and TAG_2 with some text say 'ys' and '1'. Sample file for testing the below code can be downloaded from the following link:

[sampleReplaceTagWithText.xlsx](79527942.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Replace Tag With Text Example</h1>
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

            // Parameters from original code
            const tag = "TAG_2$TAG_1";
            const replace = "1$ys";

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform replacements
            const tagParts = tag.split('$');
            const replaceParts = replace.split('$');
            tagParts.forEach((item, index) => {
                workbook.replace(`<${item}>`, replaceParts[index]);
            });

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.replace.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tags replaced successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find and Replace in Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="findText">Find:</label>
        <input type="text" id="findText" value="oldValue" />
        <label for="replaceText">Replace:</label>
        <input type="text" id="replaceText" value="newValue" />
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

        function sheetReplace(workbook, sFind, sReplace) {
            const finding = sFind;

            workbook.worksheets.forEach(sheet => {
                // Replace within sheet cells/contents
                sheet.replace(finding, sReplace);

                // Replace within page setup headers and footers (indices 0..2)
                for (let j = 0; j < 3; j++) {
                    const headerVal = sheet.pageSetup.header(j);
                    if (headerVal != null) {
                        const newHeader = headerVal.replace(finding, sReplace);
                        sheet.pageSetup.header(j, newHeader);
                    }
                    const footerVal = sheet.pageSetup.footer(j);
                    if (footerVal != null) {
                        const newFooter = footerVal.replace(finding, sReplace);
                        sheet.pageSetup.footer(j, newFooter);
                    }
                }
            });
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Loading workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sFind = document.getElementById('findText').value;
            const sReplace = document.getElementById('replaceText').value;

            // Perform find and replace across workbook
            sheetReplace(workbook, sFind, sReplace);

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
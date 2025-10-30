---
title: Hur man kontrollerar fryst tillstånd utan Excel med JavaScript via C++
linktitle: Fruset tillstånd
type: docs
weight: 190
url: /sv/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: I denna artikel lär du dig hur man programatiskt kontrollerar fryst tillstånd av ett Excel arbetsblad med JavaScript och C++ biblioteket.
---

## **Introduktion**

I denna artikel lär vi oss hur man programatiskt kontrollerar fryst tillstånd av ett Excel-arbetsblad. Vi kan enkelt avgöra om arbetsbladet är fryst eller delat i MS Excel. Men finns det ett sätt att ta reda på om det är fryst eller delat med JavaScript? Vi kan enkelt göra det med Aspose.Cells for JavaScript via C++.

## **Är fönsterfönster frysta**
Med Aspose.Cells for JavaScript via C++ kan vi kontrollera om fönstret är fryst och hur många rader och kolumner som är låsta.

Använd [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--) egenskapen för att kontrollera fönsterrutornas tillstånd och få låsta rader och kolumner med egenskapen [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--).
1. Konstruera Arbetsbok för att öppna filen.
2. Kontrollera om arbetsbladet är fruset.
3. Hämta de låsta raderna och kolumnerna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```

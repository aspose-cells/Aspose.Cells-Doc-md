---
title: Skapa arbetsbok och arbetsbladsspecifika namngivna områden med JavaScript via C++
linktitle: Namngivet intervall
type: docs
weight: 40
url: /sv/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Lär dig hur man skapar arbetsboks och arbetsbladsspecifika namngivna områden med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att definiera namngivna områden med två olika omfång: arbetsbok (också känt som globalt omfång) och arbetsblad.

- Namngivna områden med ett arbetsboksomfång kan kommas åt från vilket arbetsblad som helst inom den arbetsboken genom att helt enkelt använda dess namn.
- Arbetsbladscoped namngivna områden kommas åt med referensen till det specifika arbetsbladet där det skapades.

Aspose.Cells for JavaScript via C++ ger samma funktionalitet som Microsoft Excel för att lägga till arbetsboks- och arbetsbladsspecifika namngivna områden. När du skapar ett arbetsbladsspecifikt namn kan du använda bladreferensen i namnområdet för att specificera det som ett arbetsbladsspecifikt område.

{{% /alert %}} 
## **Lägga till ett namngivet intervall med arbetsboksuppsikt**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>WorkbookScope Named Range Example</title>
    </head>
    <body>
        <h1>WorkbookScope Named Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // If a file is provided, load it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells from Cell A1 to C10
            const workbookScope = cells.createRange("A1", "C10");

            // Assign the name to workbook scope named range
            workbookScope.name = "workbookScope";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookScope.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range "workbookScope" created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
## **Lägg till ett namngivet område med arbetsbladomfång**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Assign Range Name Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Create new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells
            const localRange = cells.createRange("A1", "C10");

            // Assign name to range with sheet reference
            localRange.name = "Sheet1!local";

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Skapa åtkomst och kopiera namngivna områden](/cells/sv/javascript-cpp/create-access-and-copy-named-ranges/)
- [Formatera och modifiera namngivna områden](/cells/sv/javascript-cpp/format-and-modify-named-ranges/)
- [Hämta intervall med externa länkar](/cells/sv/javascript-cpp/get-range-with-external-links/)
- [Implementera icke-sekventiella områden](/cells/sv/javascript-cpp/implementing-non-sequential-ranges/)

---
title: Crea intervalli nominati con ambito di cartella di lavoro e di foglio di lavoro con JavaScript tramite C++
linktitle: Intervallo Nominato
type: docs
weight: 40
url: /it/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Impara a creare intervalli nominati con ambito di cartella di lavoro e di foglio di lavoro usando Aspose.Cells for JavaScript tramite C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire intervalli nominati con due ambiti diversi: cartella di lavoro (noto anche come ambito globale) e foglio di lavoro.

- I nomi definiti con un ambito a livello di cartella di lavoro possono essere accessibili da qualsiasi foglio di calcolo all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- I nomi definiti con ambito a livello di foglio di lavoro sono accessibili con il riferimento al foglio di lavoro particolare in cui sono stati creati.

Aspose.Cells for JavaScript tramite C++ fornisce la stessa funzionalità di Microsoft Excel per aggiungere intervalli nominati con ambito di cartella di lavoro e di foglio di lavoro. Quando si crea un intervallo nominato con ambito di foglio di lavoro, si dovrebbe usare il riferimento al foglio di lavoro nel nome per specificarlo come intervallo nominato con ambito di foglio.

{{% /alert %}} 
## **Aggiunta di un intervallo con nome a livello di cartella di lavoro**


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
## **Aggiunta di un intervallo con nome a livello di foglio di lavoro**


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

## **Argomenti avanzati**
- [Crea accesso e copia intervalli con nome](/cells/it/javascript-cpp/create-access-and-copy-named-ranges/)
- [Formattare e modificare intervalli con nome](/cells/it/javascript-cpp/format-and-modify-named-ranges/)
- [Ottieni Intervallo con Link Esterni](/cells/it/javascript-cpp/get-range-with-external-links/)
- [Implementazione degli Intervallo Non Sequenziali](/cells/it/javascript-cpp/implementing-non-sequential-ranges/)

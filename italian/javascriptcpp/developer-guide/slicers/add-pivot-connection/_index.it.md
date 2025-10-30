---
title: Aggiungi connessione Pivot con JavaScript tramite C++
linktitle: Aggiungi connessione pivot
type: docs
weight: 30
url: /it/javascript-cpp/add-pivot-connection/
description: Impara come aggiungere una connessione pivot usando Aspose.Cells for JavaScript tramite C++.
keywords: Aggiungi connessione pivot senza Office 2013, Office 2016, Office 2019 e Office 365 JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi associare uno slicer e una tabella pivot in Excel, fai clic destro sullo slicer e seleziona "Connessioni rapporti...". Nell'elenco delle opzioni, puoi operare sulla casella di controllo. Se invece vuoi associare uno slicer e una tabella pivot usando ASPose.Cells API programmando, usa il metodo [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-). Il metodo assocerà lo slicer e la tabella pivot.

## **Associa Slicer e Tabella pivot**

Il seguente esempio carica il [file Excel di esempio](add-pivot-connection.xlsx) che contiene uno slicer esistente. Accede allo slicer e poi associa lo slicer e la tabella pivot. Infine, salva il file come [file Excel di output](add-pivot-connection-out.xlsx).

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

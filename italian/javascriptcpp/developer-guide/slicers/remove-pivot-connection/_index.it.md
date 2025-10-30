---
title: Rimuovere la connessione Pivot con JavaScript tramite C++
linktitle: Rimuovere la connessione pivot
type: docs
weight: 30
url: /it/javascript-cpp/remove-pivot-connection/
description: Impara come rimuovere la connessione pivot usando Aspose.Cells for JavaScript tramite C++.
keywords: Rimuovere la connessione pivot senza Office 2013, Office 2016, Office 2019 e Office 365 JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi dissociare uno slicer e una tabella pivot in Excel, è necessario cliccare con il tasto destro sullo slicer e selezionare "Connessioni report..." dall'elenco delle opzioni, puoi operare sulla casella di controllo. Allo stesso modo, se vuoi dissociare uno slicer e una tabella pivot tramite l'API Aspose.Cells for JavaScript tramite C++, utilizza il metodo [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-). Dissocierà lo slicer e la tabella pivot.

## **Dissociare lo slicer e la tabella pivot**

Il seguente esempio di codice carica il [file Excel di esempio](remove-pivot-connection.xlsx) che contiene uno slicer esistente. Accede agli slicer e poi disassociano lo slicer e la tabella pivot. Infine, salva il workbook come [file Excel di output](remove-pivot-connection-out.xlsx).

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
